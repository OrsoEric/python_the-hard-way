##  acceleration information
#   unit measure is g

#
#from datetime import datetime
import os
#import pandas
import logging
#unzip
#import zipfile
#process
#import numpy as np
import pandas as pd
#for column generation
import itertools

#import string

import datetime

import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from pandas.tseries.offsets import Second
#import matplotlib.dates as mdate
#for log color view
#from matplotlib.colors import LogNorm
#from pandas.core.frame import DataFrame

#should do progress bars?
#import tqdm

CONFIDENTIAL_DATA_FOLDER = 'confidential_datasets'
CONFIDENTIAL_DATA_FILE = "ReportACCEL__27-04-2021_06-05-2021_ID7.txt"
SAMPLING_FREQUENCY = 331.0

def fetch_data_frame( source_folder, source_filename):
    #compute filename
    file_name = os.path.join(os.getcwd(), source_folder, source_filename)
    logging.info(f"process filename: {file_name}")

    #construct the names of the columns
    my_column_names = [ "timestamp" ] + [f"{axis}{index}" for axis, index in itertools.product( "xyz", range(506))]
    #try to load a csv from the zipped file. use ID to add to the series. use the column names I generated X0...X505 Y0...Y505 Z0...Z505
    my_data_frame = pd.read_csv(file_name, sep='\t', names = my_column_names )
    my_data_frame.index = pd.to_datetime( my_data_frame['timestamp'] )
    del my_data_frame['timestamp']

    return my_data_frame

##unpack the dataframe in a list of dataframes
def unpack_accelerations( source_data_frame, frequency ):

    ##I'm stuck trying    
    samples_per_row =506
    #row name
    index = source_data_frame.index[0]

    new_index = [index +datetime.timedelta(seconds =(1.0/SAMPLING_FREQUENCY)*cnt) for cnt in range(samples_per_row)]
    new_acceleration = pd.DataFrame( index= new_index,columns=["x","y","z"])

    new_acceleration.iloc[0:samples_per_row,0] = source_data_frame.iloc[0,0:samples_per_row]
    new_acceleration.iloc[0:samples_per_row,1] = source_data_frame.iloc[0,samples_per_row:samples_per_row*2]
    new_acceleration.iloc[0:samples_per_row,2] = source_data_frame.iloc[0,samples_per_row*2:samples_per_row*3]

    #new_acceleration.index = 
    print(new_acceleration)

    #fetch the first row
    my_row = source_data_frame.loc[index].transpose()
    print(my_row)

    return
    


def main():

    my_acceleration_data = fetch_data_frame(CONFIDENTIAL_DATA_FOLDER, CONFIDENTIAL_DATA_FILE)
    logging.info(f"{my_acceleration_data}")
    #the point plot shows there are burst of acquisitions followed by inactivity. i need to separate the burst of activity. the marker shows when the points are
    #my_acceleration_data[["x1", "y1", "z1"]].plot(marker="o")
    #plt.show()

    #we lack the sample time between the samples. the index is when the burst of acquisition started

    #my_acceleration_data["timestamp"].plot.h  .index.plo

    list_of_accelerations = unpack_accelerations( my_acceleration_data, SAMPLING_FREQUENCY )

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