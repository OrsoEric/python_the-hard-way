##  Modules
#   i cannot have the linker put together pieces like c++. def needs to be executed and consumes runtime
#   a module is like a library

#i can import pieces of a module and rename them
from math import isclose, log, sqrt as math_sqrt
print("try math: ", math_sqrt( 5.0 ) )

#-------------------------------------------------------------------
#LOG default of python and good

import logging

def main():
    logging.info('for info')
    logging.debug('for debug')
    logging.warning('for warning')
    logging.error('for critical')
    logging.critical('chernobyl is happening')
    pass
    
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.DEBUG,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    
    main()

#-------------------------------------------------------------------
# math numbers
# cmath complex numbers

import math as lib_math

num = lib_math.sqrt(2.0)**2
print(f"float have approximation... equal? {2.0 == num} isclose? {lib_math.isclose(2.0, num)} |")


#-------------------------------------------------------------------
# string

import string as lib_string
print( 'ascii_lowercase: ', lib_string.ascii_lowercase )
print( 'check if a letter is ascii: ', 'è' in lib_string.ascii_letters )

#-------------------------------------------------------------------
# sys
import os
import sys as lib_sys
import warnings
#used to specify where take .py modules
print(lib_sys.copyright)

print(lib_sys.path.append(os.getcwd()))

#detect when asserts are enabled
if lib_sys.flags.optimize == 0:
    warnings.warn("Warning, all asserts are enabled", stacklevel=1)

#-------------------------------------------------------------------


os.path.join(os.getcwd(), 'dir1', 'dir2', 'foo.txt')

#terminate program with status 1
#lib_sys.exit(1)

#-------------------------------------------------------------------
#   regular expressions
#   write a family of strings as a single string

import re as lib_regex
#go to www.regex101.com

#-------------------------------------------------------------------
#   python doesn't like ensted loops. use generators
#   itertools has the facilities to 

from itertools import product
print("do two cycles 1 to 10 on 2 loops:")
for x,y in product( range(1,11), repeat=2):
    print(f'({x},{y})',end=' ')

print("\ndo three cycles on each character of a string:")
for p in product( 'ABCD', repeat=3):
    print(p,end=' ')

print("\nscan from multiple strings")
for p in product( 'ABCD', 'abcdf'):
    print(p,end=' ')

print("\npermutations on two symblos from a source string")
from itertools import permutations
for p in permutations( 'ABCD', 2):
    print(p,end=' ')

print("\ncombinations on two symblos from a source string")
from itertools import combinations
for p in combinations( 'ABCD', 2):
    print(p,end=' ')

print("\ncount is a generator that counts")
from itertools import count
my_instance = count()
print(next(my_instance),end=' ')
print(next(my_instance),end=' ')
print(next(my_instance),end=' ')

#-------------------------------------------------------------------
#random library

import random as lib_random

print('\nreturn random float between 0 and 1: ', lib_random.random() )
start = 10
stop = 99
print(f'\nreturn random int between {start} and {stop}: ', lib_random.randint(start, stop) )

print('I can save the state ')
save_state = lib_random.getstate()
print(f'\nreturn random int between {start} and {stop}: ', lib_random.randint(start, stop) )
lib_random.setstate(save_state)
print(f'\nreturn random int between {start} and {stop}: ', lib_random.randint(start, stop) )
#-------------------------------------------------------------------
 

 #import pprint

 #shaka = {'three': [2,5,4], 'mot':'hugmong'}
 #pprint(shaka)


#-------------------------------------------------------------------
# collections
# default dict has something to do with doing things faster

from collections import defaultdict, Counter
import random

numbers = [random.randint(0, 9) for _ in range(100_000)]

def a(numbers):
    count = dict()
    for n in numbers:
        if n not in count:
            count[n] = 1
        else:
            count[n] += 1
    return count

count = a(numbers)
{n: count[n] for n in sorted(count)}

def b(numbers):
    count = defaultdict(int)
    for n in numbers:
        count[n] += 1

count = b(numbers)
#{n: count[n] for n in sorted(count)}


count = Counter(numbers)
{n: count[n] for n in sorted(count)}



# Python program to demonstrate
# dictionary
 
 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("Dictionary:")
print(Dict)
print(Dict[1])
 
# Uncommenting this print(Dict[4])
# will raise a KeyError as the
# 4 is not present in the dictionary

#-------------------------------------------------------------------
# 
from collections import ChainMap

#i have two dictionaries
d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4, 'e': 19} 
d3 = {'e': 5, 'f': 6} 
    
# Defining the chainmap  
c = ChainMap(d1, d2, d3)  

print('I have all the maps together', c, c['e'])

#-------------------------------------------------------------------
# namedtuple it's like a struct. i can access with index or names, i have a fixed number of named fields

from collections import namedtuple

# Declaring namedtuple()  
Student = namedtuple('Student',['name','age','DOB'])
# Construct 
my_named_tuple = Student('Nandini','19','2541997')
# Access using index  
print(f"The Student age using index is : {my_named_tuple[1]}")
#access using keyname
print(f"The Student age using keyname is : {my_named_tuple.age}")

#-------------------------------------------------------------------

