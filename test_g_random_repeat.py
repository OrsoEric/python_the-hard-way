#NOTE: done with convert to string and str.find is much faster due to better builtin find

#python modules
from itertools import product
import calendar
import logging
import time as lib_time
import random as lib_random

##  Search a sequece of a given length that is repeated inside the source sequence
#
def search_repeat_list( source_list : list(), repeat_length : int ):
    #fetch length
    source_list_len = len(source_list)
    #lists that are too shorts are not worth searching in
    if (source_list_len <= repeat_length):
        return -1

    #initialize search
    sequence_index = 0
    repeat_index = 0
    #while search is not complete. exclude last symbol from the search as it would always HIT
    while(sequence_index +repeat_index < source_list_len -1):
        #if the symbol in the mask matches the symbol in the sequence
        if (source_list[source_list_len -repeat_length +repeat_index] == source_list[sequence_index +repeat_index]):
            #try to match the next mask symbol
            repeat_index += 1
            #check if all symbols in the mask have been matched
            if (repeat_index >= repeat_length):
                #I have a repetition
                return sequence_index
        #if i do not match
        else:
            #start matching from first symbol in the sequence
            repeat_index = 0
            #match the next symbol in the sequence
            sequence_index += 1

    return -1

##
#   measure how long it takes for a sequence of a given length to repeat
#   length of repeat sequence
#   min
#   max
#   use the more compact search algorithm
def measure_repeat( min : int, max : int, length : int ) -> int:
    """measure how long it takes for a sequence of a given length to repeat
    """
    #snap start
    start = lib_time.time()
    #initialize sequence list
    my_sequence = list()
    #while a repeat is not found
    while True:
        #generate a random number
        temp = lib_random.randint(min, max)
        #add the number to a sequence
        my_sequence.append( temp )
        #check if adding the number causes a repeat
        index = search_repeat_list( my_sequence, length )
        #if a repeat has been found
        if index >= 0:
            #measure time elapsed
            time_elapsed = lib_time.time() -start
            logging.info(f'execution time: {time_elapsed}, sequence length: {len(my_sequence)}')
            logging.info(f'index : {index} | sequence: {my_sequence[index:index+length]}')
            logging.info(f'index : {len(my_sequence)-length} | sequence: {my_sequence[-length:]}')
            return len(my_sequence)
        else:
            pass
    
    return 0

def measure_performance( min_rand, max_rand, max_sequence_length, num_seeds ):
    #
    min_sequence_length = 2
    old_seed = 0
    my_seed = int()
    #scan both the sequence length and the seed
    for sequence_length, seed_index in product(range( min_sequence_length, max_sequence_length+1), range(0, num_seeds)):
        #reset the list of random numbers
        my_sequence = list()
            #ROLL A SEED
        #roll a new seed from epoch
        my_seed = calendar.timegm(lib_time.gmtime())
        print(my_seed)
        #check if seed has changed, otherwise increment previous seed
        if (my_seed == old_seed):
            my_seed += 1
        #apply the seeds
        lib_random.seed(my_seed)
        old_seed = my_seed

            #LAUNCH A SEARCH
        measure_repeat( min_rand, max_rand, sequence_length)


    return None

## main
def main():

    #make sure the seed is the same for all
    my_seed = 42
    lib_random.seed(my_seed)
    logging.info(f'seed: {my_seed}')

    #test submodule
    #print(is_repeat( [5, 7, 3, 5, 7] , 2 ))
    #test more compact list search
    #print( search_repeat_list([2, 5, 7, 3, 5, 7] , 2) )

    #execute
    #sequence_length = measure_repeat( 1, 90, 3 )
    #print('', sequence_length)

    measure_performance(1, 90, 3, 2)
    
    #print(f'elapsed time: {- start}')
    pass

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.INFO,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()