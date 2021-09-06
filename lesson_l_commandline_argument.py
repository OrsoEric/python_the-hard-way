
import os
import sys
import warnings
import logging
#hugely complicated modules
import argparse


## 
#
def main():
    return None

## 
#
if __name__ == '__main__':
    #
    logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.INFO)
    #build a parser
    parser = argparse.ArgumentParser()
        #add command line arguments
    #debuf. -d will put a value of 2 in verbose
    parser.add_argument('-d',
                        '--debug',
                        action='store_const',
                        dest='verbose',
                        const=2,
                        help='log debug messages (same as -vv)')
    #verbose. will count. -vvv will set var to 3. by default use same var name as extended option, so verbose
    parser.add_argument('-v', '--verbose', action='count', default=0, help='increase log verbosity')
    #argument with parameter
    parser.add_argument('-s', '--shaka', nargs=1, help='When the walls fell')
    #???
    parser.add_argument('args', nargs='+', metavar='data_file', help='data files')

    #ask parser to parse the arguments
    args = parser.parse_args()
    #return a named tuple
    if args.verbose == 0:
        logging.getLogger().setLevel(level=logging.WARNING)
    elif args.verbose == 1:
        logging.getLogger().setLevel(level=logging.INFO)
    elif args.verbose == 2:
        logging.getLogger().setLevel(level=logging.DEBUG)
    logging.debug(f'log level: {args.verbose}')
    logging.debug(f': {args.shaka}')

    #detect opimization level
    if sys.flags.optimize == 0:
        warnings.warn("Warning, all asserts are enabled", stacklevel=1)

    main()

