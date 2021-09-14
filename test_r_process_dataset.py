#for perf_counter
import time
import logging
import matplotlib.pyplot as plt
import seaborn as sns
#import datetime
#to format float inot an engineering format string
from float_to_eng_string import float_to_eng_string

#numpy
timestamp = time.perf_counter()
import numpy as np
print(f'took {float_to_eng_string(time.perf_counter() -timestamp)}s to import numpy')

#pandas
timestamp = time.perf_counter()
import pandas as pd
print(f'took {float_to_eng_string(time.perf_counter() -timestamp)}s to import pandas')

CONFIDENTIAL_DATA = 'confidential_datasets//ReportPT100_21042021_17_12_19_ID24.txt'

#logging.debug(f"{}")
def main():
    #make sure the file can be opened
    #with open(CONFIDENTIAL_DATA) as my_file:
    #    logging.debug(f"{my_file}")
    
    my_csv = pd.read_csv(CONFIDENTIAL_DATA, header=None, sep='\t', names = ['timestamp', 't1', 't2'])
    logging.info(f"csv file: {my_csv}")
    print(my_csv)

    #i could do it with datetime module
    #print( f"{temp_string} | { datetime.datetime.strptime(temp_string,'%Y-%m-%d %H:%M:%S')}" )

    #pd has a module that does it
    #for temp_string in my_csv.timestamp:
        #print( f"{temp_string} {pd.to_datetime(temp_string) }")

    #i can feed the whole column
    #print( f"{pd.to_datetime(my_csv['timestamp']) }")

    #i can use my datestamp as index
    my_csv.index = pd.to_datetime(my_csv['timestamp'])
    print(f"type {my_csv['timestamp']} | type {my_csv.index}")

    #i can now destroy the timestamp
    del my_csv['timestamp']

        
    #filter: i replace outliers with nan
    my_csv.loc[((my_csv.t1 < -20) | (my_csv.t1>100)), 't1'] = np.nan
    my_csv.loc[((my_csv.t2 < -20) | (my_csv.t2>100)), 't2'] = np.nan

    #this would remove all nan. this discarded information
    #my_csv.dropna(inplace = True)

    #i want to interpolate the nan
    my_csv.interpolate(inplace = True, method='time')

    #print(my_csv.timestamp )
    #my_csv.loc['timestamp',:] = datetime.datetime.strptime(my_csv.loc['timestamp',:],"%d/%m/%Y %H:%M")
    print(my_csv)
    #plt.subplot(1, 2, 1)
    my_csv.plot()

    #plt.subplot(1, 2, 2)
    my_csv.plot.hist()


    plt.show()

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        #level=logging.INFO,
        level=logging.DEBUG,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()
    

