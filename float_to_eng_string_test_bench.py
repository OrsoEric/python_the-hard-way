#used to log
import logging
#import the function that performs the conversion
from float_to_eng_string import float_to_eng_string

def main():
    #assert not ((digit_int < 0) or (digit_int > 9)), f"ERR {digit_int} {digit}"
    #core test
    #test_vector = [ 234.56 ]
    #test_vector = [ 999.99999 ]
    #test_vector = [ 0.33 ]
    #test_vector = [ 99.999999 ]
    test_vector = [0.1, 0.33, 1.0, 3.34, 9.99999, 10.0, 33.412, 99.999999, 100.0, 345.6, 456.123, 456.789, 999.99999, 1000.00001, 5000.0, 60000.0, 700000.0, 999999.999999, 1000000.000009]
    for value in test_vector:

        temp_str = float_to_eng_string(value)
        try:
            temp_float = float(temp_str[:-1])
        except:
            temp_float = 0.0
        if temp_str[-1] == 'm':
            temp_float /= 1000.0

        print("---------------------------------")
        print(f"Value: {value} | Eng: {temp_str} -> ERR: {value -temp_float}")
        print("---------------------------------")

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        #level=logging.DEBUG,
        level=logging.INFO,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()
