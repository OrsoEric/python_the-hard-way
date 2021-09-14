#for perf_counter
import time
#to format float inot an engineering format string
from float_to_eng_string import float_to_eng_string

#numpy
timestamp = time.perf_counter()
import numpy as np
print(f'took {float_to_eng_string(time.perf_counter() -timestamp)}s to import numpy')

#scipy
timestamp = time.perf_counter()
import scipy as lib_scipy
print(f'took {float_to_eng_string(time.perf_counter() -timestamp)}s to import scipy')

#pandas
timestamp = time.perf_counter()
import pandas as pd
print(f'took {float_to_eng_string(time.perf_counter() -timestamp)}s to import pandas')

##
#   used by data scientists
#   Keys: Series, DataFrame
#   advised workflow
#   excel -> pandas to import and show -> numpy to process -> give result back to pandas to show


def test_series():
    my_series = pd.Series(np.random.randint(1, 11, (4,)))
    print(f"from list to pd.series\n {my_series}")

    my_series = pd.Series([666, 42], index=["beast", "answer"])
    print(f"series have keys like maps:\n {my_series}")

    search = ["beast", "grey", "answer", "cotton"]
    my_new_series = pd.Series(my_series, search)
    print(f"inherit into a new series with keys, missing are NaN:\n {my_new_series}")

    my_new_series.name = "Gods"
    print(f"series have a name:\n {my_new_series}")

##
# it's a set of ordered columns    
def test_data_frames():
    #initialize from a dictionary
    my_data_frame = pd.DataFrame( {"name" : ["Hugh", "Biggus", "Mike" ], "surname": ["Mongous", "Diccus", "Hunt"]})
    print(f" {my_data_frame}")



#test_series()
test_data_frames()