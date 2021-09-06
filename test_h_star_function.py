import logging

## 
# min
# max
def minmax_scrubber( min : int, max : int, /, *args, equal_minor = True, equal_major = True) -> list():
    """get min, max than a sequence of numbers. returns all numbers between min and max
    example: minmax_scrubber(10, 20, 9, 13, 99) -> [13]
    option: equal_minor and equal_major will activate deactivate scrubbing numbers equal to min or max
    """
    #initialize list
    scrubbed_values = list()

    #with loop
    #for value in args:
        #if (min <= value <= max):
            #scrubbed_values.append(value)

    #with list comprehension
    scrubbed_values = [value for value in args if (min < value < max) or (equal_minor == True and value == min) or (equal_major == True and value == max)]
        
    #return scrubbed list
    return scrubbed_values

##
def main():
    #test with strict
    scrubbed = minmax_scrubber(10, 20, 9, 13, 99, 17, 20, 10) 
    print(scrubbed ) 
    scrubbed = minmax_scrubber(10, 20, 9, 13, 99, 17, 20, 10, equal_major=False) 
    print(scrubbed ) 
    scrubbed = minmax_scrubber(10, 20, 9, 13, 99, 17, 20, 10, equal_minor=False) 
    print(scrubbed ) 
    scrubbed = minmax_scrubber(10, 20, 9, 13, 99, 17, 20, 10, equal_major=False , equal_minor=False) 
    print(scrubbed ) 

    #i can use star operator to unpack lists as individual values
    scrubbed = minmax_scrubber( 10, 20, *range(1, 100) ) 
    print(scrubbed ) 

    return None

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.INFO,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()
