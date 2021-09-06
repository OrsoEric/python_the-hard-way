import logging

## get min, max than a sequence of numbers. returns all numbers between min and max
# min
# max
# 10, 20, 9, 13, 99 -> 13
def minmax_scrubber( min : int, max : int, /, *args) -> list():
    scrubbed_values = list()
    #with loop
    #for value in args:
        #if (min <= value <= max):
            #scrubbed_values.append(value)

    #with list comprehension
    scrubbed_values = [value for value in args if min <= value <= max]
        
    return scrubbed_values

##
def main():
    scrubbed = minmax_scrubber(10, 20, 9, 13, 99, 17) 
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
