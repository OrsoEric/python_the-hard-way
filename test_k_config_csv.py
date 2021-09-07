## combine a INI configuration file and a CSV module to read a .csv file
#using spaces/tab as separator is dumb. changed editor settings to force tab

#for computation of path
import os
#used to log
import logging
#used to load an INi
import configparser
#csv load library
import csv

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
            return -1

    #failed to find section
    else:
        logging.error(f"section >{ini_sections}< doesn't exist...")
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


    return

##
#
def main():
    """main...."""

    #sections and keys used that MUST be present in the INI file
    ini_sections = "path"
    ini_keys = ["csv_subfolder", "csv_file", "csv_header" ]
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
    csv_header = ret[ini_sections][ini_keys[2]]
    logging.debug( f"csv has header? {csv_header}")

    #open the csv file
    my_csv = load_csv_file( csv_filename )
    
    #process the csv file
    process_csv(my_csv, csv_header)

    return 0

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.DEBUG,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()