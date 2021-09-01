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

import sys as lib_sys

print(lib_sys.copyright)

#terminate program with status 1
#lib_sys.exit(1)

#-------------------------------------------------------------------
#   regular expressions
#   write a family of strings as a single string

import re as lib_regex

#-------------------------------------------------------------------
