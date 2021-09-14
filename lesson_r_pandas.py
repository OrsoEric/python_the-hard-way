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
    my_data_frame = pd.DataFrame( {"name" : ["Hugh", "Biggus", "Mike" ], "surname": ["Mongous", "Diccus", "Hunt"], "Key":[42, 666, 0]})
    print(f"Data Frame:\n{my_data_frame}")
    print(f"dot operator with field name extract a series:\n{my_data_frame.name}")
    
    #dictionaries of dictionaries
    population_dictionary_of_dictionary = { "Italy" : {2000 : 60e6, 2010: 65e6, 2020: 70e6, 2030: 517}, "Sealand" : { 2000 : 5, 2005: 5, 2015: 5, 2020: 5, 2029: 7} }
    my_data_frame = pd.DataFrame( population_dictionary_of_dictionary )
    print(f"from dictionaries of dictionaries. shared keys, missing NaN:\n{my_data_frame}")
    my_data_frame.Index = "Population history"
    print(f"Data Frame Index:\n{my_data_frame.index}")

    #care not usign weird keys
    #poison_data_frame = { "index" : [40, 50], "finger": [8]}
    #poison_data_frame.Index = "hand"
    #print(f"Data Frame Index:\n{poison_data_frame.index} {poison_data_frame}")

#print(f"{}")
def test_df_loc():
    data_frame_pop = pd.DataFrame({ "Italy" : {2000 : 60e6, 2010: 65e6, 2020: 70e6, 2030: 517}, "Sealand" : { 2000 : 5, 2005: 5, 2015: 5, 2020: 5, 2029: 7} })
    print(f"Data Frame:\n{data_frame_pop}")
    print(f"loc allow to use square brackets like numpy: {data_frame_pop.loc[2000]}")
    print(f"loc allow construction of a numpy subset array: {  data_frame_pop.loc[[2000, 2015], ['Italy']] }")


def test_drop():
    data_frame_pop = pd.DataFrame({ "Italy" : {2000 : 60e6, 2010: 65e6, 2020: 70e6, 2030: 517}, "Sealand" : { 2000 : 5, 2005: 5, 2015: 5, 2020: 5, 2029: 7} })
    print(f"Data Frame:\n{data_frame_pop}")
    data_fram_drop = data_frame_pop.drop[2020]
    print(f"drop does an hard copy by default: {data_frame_pop}")    



#test_series()
#test_data_frames()
#test_df_loc()
#test_drop()


