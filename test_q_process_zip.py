#
import os
#import pandas
import logging
#unzip
import zipfile
#process
import pandas as pd

import string

CONFIDENTIAL_DATA_FOLDER = 'confidential_datasets'
CONFIDENTIAL_DATA_FILE = '210521_36000_45_4Nm_txt.zip'

##  Try to open a file
def try_to_open( file_name : str() ) -> bool:
    try:
        with open(file_name) as opened_file:
            return False
    except OSError as problem:
        logging.error(f"ERR Could not open file: {problem}")

    return True
##  Process a file inside a zip
#
def exercise1_zip() -> bool:
    #compute filename
    file_name = os.path.join(os.getcwd(), CONFIDENTIAL_DATA_FOLDER, CONFIDENTIAL_DATA_FILE)
    logging.debug(f"process filename: {file_name}")
    #try to open file
    x_success = try_to_open(file_name)
    if (x_success == True):
        logging.error(f"ERR Could not open file: {file_name}")
        return True
    #try to use the zipfile module to open and unzip the file, automatically close when done
    with zipfile.ZipFile(file_name) as zipped_file:
        #for every file name that class zipped was able to unzip
        for unzipped_file_name in zipped_file.namelist():
            #I can process the filename to extract the datetime and ID
            #sample
            #>ReportPT100_07052021_18_11_58_ID10
            #>ReportPT100_07052021_18_11_58_ID3
            #>ReportPT100_07052021_18_11_58_ID30
            #split string as chunks
            string_split = unzipped_file_name.split('_')
            string_datetime = string_split[1]+' '+string_split[2] +':'+string_split[3] +':'+string_split[4]
            string_id = string_split[5][2:-4]
            file_datetime = pd.to_datetime( string_datetime, format='%d%m%Y %H:%M:%S' )
            file_id = int(string_id)
            logging.info(f"unzipped file: {unzipped_file_name} | Datetime: {file_datetime} | ID: {file_id}")
            
            #try to load a csv from the zipped file
            my_data_frame = pd.read_csv(zipped_file.open(unzipped_file_name), sep='\t', names=['Datetime', 't1', 't2'] )
            my_data_frame.index = pd.to_datetime( my_data_frame['Datetime'] )
            del my_data_frame['Datetime']

            #print(my_data_frame)
            #try:
                
            #except:
                #logging.error(f"ERR: could not open zipped file {unzipped_file_name}")

def main():

    exercise1_zip()
    pass

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.DEBUG,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()