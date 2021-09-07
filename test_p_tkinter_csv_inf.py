## combine a INI configuration file and a CSV module to read a .csv file
#using spaces/tab as separator is dumb. changed editor settings to force tab
#add message box for missing fields in the INI file

#for computation of path
import os
#used to log
import logging
#used to load an INi
import configparser
#csv load library
import csv
#average
import statistics
#convert iso format date
import datetime
#to show error windows
import tkinter as tk
from tkinter import messagebox

##  Globals
CONFIG_FILE = 'test_k_config.ini'

## Load the configuration file
#
def load_config_file( filename_config : str(), ini_sections, ini_keys : list() ):
    """load configuration file
    checks that a list of sections and a list of keys are contained inside the INI
    return the INI file
    """
    #construct path
    my_ini_filename = os.path.join(os.getcwd(), filename_config)
    #construct config parser
    my_ini = configparser.ConfigParser()
    #try to load the configuration file    
    try:
        with open(my_ini_filename) as my_opened_ini:
            #use the configparser to parse the INI
            my_ini.read_file(my_opened_ini)
            #method .read get a path

    #failed to open file
    except OSError as problem:
        logging.error(f'problem: {problem}')
        return -1

    #search a given section inside the INI (inside square brackets [section])
    logging.debug(f'see the sections of the INI: {my_ini.sections()}')
    if ini_sections in my_ini.sections():
        #search a given key inside the section
        #fetch attributes inside the section and pu them inside an iterable list
        target_section_attributes = list(my_ini[ini_sections])
        logging.debug(f"section {ini_sections} exist! and contain: {target_section_attributes}")
        #search if keys exist
        if all(key in target_section_attributes for key in ini_keys):
            #show the key and value
            logging.debug(f"attribute >{ini_keys}< exist and is equal to: {my_ini.items(ini_sections, ini_keys)}")
        #failed to find key inside section
        else:
            logging.error(f"attribute >{ini_keys}< doesn't exist...")
            messagebox.showerror("Missing Key", f"INI key {ini_keys} required")
            return -1

    #failed to find section
    else:
        logging.error(f"section >{ini_sections}< doesn't exist...")
        messagebox.showerror("Missing Section", f"INI section {ini_sections} required")
        return -1

    return my_ini

##
#
def load_csv_file( csv_file_path : str() ):
    """load a csv in a given directory"""

    #PROCESS 
    logging.debug(f"file_name: {csv_file_path}")

    try:
        with open(csv_file_path) as csv_file:
            #try to autodetect the dialect of the csv by reading a number of bytes
            #autodetect_dialect = csv.Sniffer.sniff( csv.Sniffer(), sample=csv_file.read(2**10) )
            autodetect_dialect = csv.Sniffer().sniff( sample=csv_file.read(2**10) )
            #reset the file to restart from the beginning
            csv_file.seek(0)
            #process the rows one at a time as csv and push them
            my_csv = [row for row in csv.reader(csv_file, dialect=autodetect_dialect)]
            logging.debug(f"dialect delimiter: >{autodetect_dialect.delimiter}< | csv: {my_csv[:5]}")


    except OSError as problem:
        logging.error(f"Problem: {problem}")
        return -1

    return my_csv

##
#
def process_csv( source_csv : list(), is_header : bool = True  ):
    """process a csv structure"""

    #logging.debug(f"{source_csv}")
    
    #process header
    if is_header == True:
        start_index = 1
    else:
        start_index = 0
    logging.debug(f"start_index: {start_index}") 
    #separate the columns in their own lists
    timestamp_list = list()
    temperature_list = list()
    #scan all data rows
    for row in source_csv[start_index:]:
        timestamp_list.append( row[0] )
        try:
            #try to convert to float
            temperature_list.append( float(row[1]) )
        except:
            #maybe the user is using comma instead of dots
            row[1] = row[1].replace(",", ".")
            try:
                temperature_list.append( float(row[1]) )
            except:
                #if fail
                logging.critical(f"cannot convert to float {row[1]}")
                temperature_list.append( -273.15 )
                return -1

    logging.debug(f"timestamp_list snippet: {timestamp_list[:4]}") 
    logging.debug(f"temperature_list snippet: {temperature_list[:4]}") 

    #check if the temperature is within expected range
    temperature_min = 0.0
    temperature_max = 100.0
    #print(any(temperature_min > reading or temperature_max > reading for reading in temperature_list))
    #if any( temperature_min < reading or reading > temperature_max for reading in temperature_list):
    #if any( temperature_min < reading > temperature_max for reading in temperature_list):
        #logging.error(f"a temperature is outside expected range {temperature_min} {temperature_max} {[ reading for reading in temperature_list if reading < temperature_min or reading > temperature_max ]}")
        #logging.error(f"a temperature is outside expected range {temperature_min} {temperature_max} {[reading for reading in temperature_list if temperature_min < reading > temperature_max ]}")
        #return -1

    
    logging.debug(f"temperature {[reading for reading in temperature_list if (temperature_min > reading > temperature_max) ]}")
    logging.debug(f"temperature {[reading for reading in temperature_list if (reading < temperature_min or reading > temperature_max) ]}")

    #convert timestamp in ISO format
    for index, timestamp in enumerate(timestamp_list):
        timestamp_list[index] = datetime.datetime.strptime(timestamp,"%d/%m/%Y %H:%M")
    

    #replace bad temperaures with the average of what came before and after
    #scan list
    for index, reading in enumerate(temperature_list):
        #if bad data
        if index != 0 and ((reading < temperature_min) or (reading > temperature_max)):
            temperature_list[index] = statistics.mean( [ temperature_list[index-1], temperature_list[index+1] ] )
            logging.debug(f"replaced bad temperature {reading} at index {index} with {temperature_list[index]}")

    
    


    return timestamp_list, temperature_list

def csv_writer( filename: str(), timestamp_list : list(), temperature_list : list() ):

    #print(csv.list_dialects())
    try:
        with open(filename, 'w+', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for timestamp, temperature in zip(timestamp_list, temperature_list):
                writer.writerow( [timestamp, temperature] )

        
    except OSError as problem:
        logging.error(f"Problem: {problem}")
        return -1


    return 0

##
#
def main():
    """main...."""

    #sections and keys used that MUST be present in the INI file
    ini_sections = "path"
    ini_keys = ["csv_subfolder", "csv_file_input", "csv_file_output", "csv_header" ]
    #load the INI file
    ret = load_config_file( CONFIG_FILE, ini_sections , ini_keys )
    #if return an integer
    if isinstance(ret, int) and ret < 0:
        logging.error(f'could not load INI file {CONFIG_FILE}...')
        return -1
    #if return something other than a configparser
    elif isinstance(type(ret), type(configparser.ConfigParser()) ):
        logging.error(f'{type(ret)} NOT a {type(configparser.ConfigParser())}... ')
        return -1
    else:
        pass

    #process INI into a usable path
    #show the path to the csv file
    logging.debug( f" path to the csv from INI: {ret.items('path', 'csv_file')}")
    csv_filename = [ ret[ini_sections][ini_keys[0]], ret[ini_sections][ini_keys[1]] ] 
    csv_filename = os.path.join(os.getcwd(), *csv_filename)
    logging.debug( f" path to the csv: {csv_filename}")

    #
    csv_header = ret[ini_sections][ini_keys[3]]
    if (csv_header == "True"):
        csv_header = bool(True)
    elif (csv_header == "False"):
        csv_header = bool(False)
    else:
        logging.error(f"Invalid INI {ini_keys[3]} : {csv_header}")
        return -1

    logging.debug( f"csv has header? {csv_header}")

    #open the csv file
    my_csv = load_csv_file( csv_filename )
    
    #process the csv file
    my_timestamp_list, my_temperature_list = process_csv(my_csv, csv_header)

    #process INI into a usable path
    #show the path to the csv file
    logging.debug( f" path to the csv from INI: {ret.items('path', 'csv_file')}")
    csv_filename = [ ret[ini_sections][ini_keys[0]], ret[ini_sections][ini_keys[2]] ] 
    csv_filename = os.path.join(os.getcwd(), *csv_filename)
    logging.debug( f" path to the csv: {csv_filename}")
    output_csv_filename = os.path.join(os.getcwd(), csv_filename)
    csv_writer(output_csv_filename, my_timestamp_list, my_temperature_list )

    return 0

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    #initialize logging
    logging.basicConfig(
        #level of debug to show
        level=logging.DEBUG,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    #retire root window
    root = tk.Tk()
    root.withdraw()
    #execute
    main()