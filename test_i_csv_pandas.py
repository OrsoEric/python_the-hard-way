
#
import os
#import pandas
import logging
from collections import namedtuple

file_name = os.path.join(os.getcwd(), 'data_files', 'benchmarks.csv')
print(f'path: {file_name}')

#
#my_csv = pandas.read_csv(my_csv_filename)
#print(my_csv)

#print("slice: ", my_csv[0:])

import csv

data = list()
try:
    with open(file_name) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(2**11))
        csv_file.seek(0)
        reader = csv.reader(csv_file, dialect=dialect)
        first_line = next(reader)
        Record = namedtuple('Record', [s.replace(' ', '_') for s in first_line])
        for r in reader:
            try:
                data.append(Record(*r))
            except:
                logging.warning(f"Sklipping line: {repr(r)}")
except OSError as problem:
    logging.error(f"Yeuch: {problem}")

print (data)