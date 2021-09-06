##  import a csv and read the data
#
import os
from collections import namedtuple

import statistics

#get path to the file
my_csv_filename = os.path.join(os.getcwd(), 'data_files', 'benchmarks.csv')
print(my_csv_filename)

#fetch the file
try:
    with open(my_csv_filename) as my_opened_csv:
        data = my_opened_csv.readlines()
except OSError as problem:
    print('problem', problem)

#extract the headers by splitting first row along the separator
header = data[0].split(';')
#i need to strip whitespaces from the header
stripped_header = list()
for name in header:
    name = name.replace(' ', '_').strip('\n')
    stripped_header.append(name)

print(stripped_header)

#Csv_header = namedtuple('header', stripped_header)
#process the remaineder
#for data_row in data[1:]:
#    my_preprocessed_csv = Csv_header(data_row)
#    print(my_preprocessed_csv)

#initialize csv
preprocessed_csv = list()
preprocessed_csv.append( stripped_header )
#for all data rows
for row in data[1:]:
    #split fields
    #print(f'process: {row}')
    split_row = row.split(';')
    #print(f'split: {split_row}')
    #for all entries
    for entry in split_row:
        #print(f'entry: {entry}')
        #compose the preprocessed file
        pass
    
    preprocessed_csv.append(split_row)


#print(preprocessed_csv)

index = 0
#seek column names
for seek in stripped_header:
    if (seek == 'QUALITY_MEASURE'):
        index +=1

## Median of Quality score when quality measure equal linear-priority
column_quality_measure = 6
column_quality_score = 7
#prepare array to hold median values
median_list = list()
#for each row
for row in preprocessed_csv[1:]:
    #if row is valid
    if len(row) > 1:
        #if match
        if (row[column_quality_measure] == 'linear-priority'):
            #print('AH!')
            #boilerplate. function needs float
            median_list.append(float(row[column_quality_score]))
        else:
            pass
    
print(median_list)

quality_score_median = statistics.median(median_list)
print(quality_score_median)




