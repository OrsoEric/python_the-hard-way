#
from datetime import datetime
import os
#import pandas
import logging
#unzip
import zipfile
#process
import numpy as np
import pandas as pd

import string

import matplotlib.pyplot as plt
import matplotlib.dates as mdate
#for log color view
from matplotlib.colors import LogNorm
from pandas.core.frame import DataFrame

#should do progress bars?
import tqdm

CONFIDENTIAL_DATA_FOLDER = 'confidential_datasets'
CONFIDENTIAL_DATA_FILE = '210521_36000_45_4Nm_txt.zip'
#CONFIDENTIAL_DATA_FILE = '36000_45_4Nm_txt.zip'

##  Try to open a file
def try_to_open( file_name : str() ) -> bool:
    try:
        with open(file_name) as opened_file:
            return False
    except OSError as problem:
        logging.error(f"ERR Could not open file: {problem}")

    return True

def parse_zipped_filename( filename : str() ):
    string_split = filename.split('_')
    #if was unable to match
    if (len(string_split) < 5):
        #skip this for loop
        return [datetime(), -1]
    string_datetime = string_split[1]+' '+string_split[2] +':'+string_split[3] +':'+string_split[4]
    string_id = string_split[5][2:-4]
    file_datetime = pd.to_datetime( string_datetime, format='%d%m%Y %H:%M:%S' )
    file_id = int(string_id)
    logging.debug(f"unzipped file: {filename} | Datetime: {file_datetime} | ID: {file_id}")
    return file_id

def fetch_data_frame_from_zip():
    #compute filename
    file_name = os.path.join(os.getcwd(), CONFIDENTIAL_DATA_FOLDER, CONFIDENTIAL_DATA_FILE)
    logging.debug(f"process filename: {file_name}")
    #try to open file
    x_success = try_to_open(file_name)
    if (x_success == True):
        logging.error(f"ERR Could not open file: {file_name}")
        return True
    #initialize list of all dataframes
    #data_frames = pd.DataFrame()
    list_of_data_frames = list()
    #try to use the zipfile module to open and unzip the file, automatically close when done
    with zipfile.ZipFile(file_name) as zipped_file:

        #I want to sort the files by ID
        zipped_file_names = zipped_file.namelist()
        
        #for every file name that class zipped was able to unzip
        for unzipped_file_name in tqdm.tqdm( sorted( zipped_file_names, key=parse_zipped_filename ) ):
            #I can process the filename to extract the datetime and ID
            #sample
            #>ReportPT100_07052021_18_11_58_ID10
            #>ReportPT100_07052021_18_11_58_ID3
            #>ReportPT100_07052021_18_11_58_ID30
            #split string as chunks
            file_id = parse_zipped_filename(unzipped_file_name)
            
            #try to load a csv from the zipped file. use ID to add to the series
            my_data_frame = pd.read_csv(zipped_file.open(unzipped_file_name), sep='\t', names=['Datetime', f'Node {file_id} Temp 1', f'Node {file_id} Temp 2'] )
            my_data_frame.index = pd.to_datetime( my_data_frame['Datetime'] )
            del my_data_frame['Datetime']

            #data_frames = pd.concat(my_data_frame)
            list_of_data_frames.append(my_data_frame)
            #print(my_data_frame)

    logging.debug(list_of_data_frames)
    logging.info(f"type: {type(list_of_data_frames)}")
    #from a list concatenate and consolidate all data frames
    data = pd.concat(list_of_data_frames)
    return data

def show_data( data : pd.DataFrame() ):
    my_figure, my_axis = plt.subplots(figsize=(16,9)) 
        
    #show grid and larger image, use an aux scale for some
    #sub_data.plot(ax =my_axis,  figsize=(16,9),grid=True, secondary_y =[ data.columns[-2],data.columns[-1]])
    #data.plot(ax =my_axis,  figsize=(16,9),grid=True, secondary_y =sub_component_b)
    data.plot(ax =my_axis,  figsize=(16,9),grid=True)
        #since X axis was a datetime there are objects that do formatting
    #set vertical line each day
    my_axis.xaxis.set_major_locator(mdate.DayLocator())
    #set vertical line each 4 hours
    my_axis.xaxis.set_minor_locator(mdate.HourLocator(interval=4))
    my_axis.xaxis.grid(True,which='minor',linestyle="--")
    #for my_minor_x_tick in my_axis.xaxis.get_minorticklocs():
    #    my_axis.axvline(x=my_minor_x_tick, ls='--')

    #set labels. 
    my_axis.xaxis.set_minor_formatter(mdate.DateFormatter('%H'))

    plt.show()
    

##  Process a file inside a zip
#
def exercise1_zip():
    #fetch data and push them inside the DataFrame
    data = fetch_data_frame_from_zip()
    logging.info(data.describe())
    #process the data
    process_data(data)
    logging.info(data.describe())
    #plot the data
    #data.plot()
    #only plot first and last columns
    sub_data = data[[data.columns[0], data.columns[1], data.columns[-2], data.columns[-1]]]
    show_data(data)
    #I need two sets of brackets or it doesn't generate a data frame in output?
    #post_process_column(data[[data.columns[0]]])
    
import seaborn as sns

##  Process a file inside a zip
#
def exercise2_correlation():
    #fetch data and push them inside the DataFrame
    data = fetch_data_frame_from_zip()
    #the data represent different components
    sub_component_a = list(data.columns[0:30])
    sub_component_b = list(data.columns[30:])
    data[data.columns[0]] += 10*np.random.random((data.shape[0],))
    
    for column_name in sub_component_b:
        del(data[column_name])
    logging.info(data.describe())
    #process the data
    process_data(data)
    logging.info(data.describe())
    #plot the data
    data.plot()
    #only plot first and last columns
    sub_data = data[[data.columns[0], data.columns[1], data.columns[-2], data.columns[-1]]]
    show_data(data)
    #find matrix of correlation
    logging.info(f"correlation:\n{data.corr()}")

    sns.heatmap(data.corr(), norm=LogNorm())
    plt.show()

##
#
def process_data( source : pd.DataFrame() ):
    #i need to sort indexes by time to make sure time interpolation to work
    source.sort_index(inplace=True)
    #
    RANGE = 5.0
    source_mean = source.mean()
    source_mean_min = min(source_mean)
    source_mean_max = max(source_mean)
    logging.info(f"mean: {source_mean}, mean min: {source_mean_min}, mean max: {source_mean_max}")
    logging.info(f"remove values {RANGE} below or above")
    for column_name in source.columns:
        #logging.info(f"cleanup column: {column_name}")
        source.loc[((source[column_name] < source[column_name].mean() -RANGE) | (source[column_name] > source[column_name].mean() +RANGE)), column_name] = np.nan

    source.interpolate(inplace = True, method='time')

    return

##
def post_process_column( source : pd.DataFrame() ):
    logging.info(f"postprocess source:\n{source}")
    #add a column which is the difference of
    column_name = source.columns[0]
    logging.info(source.describe())
    #compute difference
    source["shaka"] = np.abs( source[column_name] -source[column_name].shift() )
    
    #scrub derivatives that are too high
    MAX_DIFF = 2.5
    source.loc[(source["shaka"] > MAX_DIFF), column_name] = np.nan
    #delet aid column
    del(source["shaka"])
    logging.info(f"postprocess source:\n{source}")
    return

##
def main():
    exercise2_correlation()
    
    pass

## if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.INFO,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()