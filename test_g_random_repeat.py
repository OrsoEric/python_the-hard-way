import random as lib_random

##
#   measure how long it takes for a sequence of a given length to repeat
#   length of repeat sequence
#   min
#   max
#   seed
def measure_repeat( min : int, max : int, length : int ) -> int:
    
    #initialize sequence list
    my_sequence = list()
    #while a repeat is not found
    while True:
        #generate a random number
        temp = lib_random.randint(min, max)
        #add the number to a sequence
        my_sequence.append( temp )
        #check if adding the number causes a repeat
        if is_repeat( my_sequence, length ) == True:
            print('DONE: ', my_sequence)
            return len(my_sequence)
        else:
            pass
    
    return 0

##
#   check if adding this number to a sequence causes a repeat with a sequence of length L. the test sequence is at the end.
def is_repeat( source_sequence : list(), sequence_length : int ) -> bool:

    #if source sequence is too short
    if sequence_length >= len(source_sequence):
        #cannot repeat
        return False

    #generate the mask sequence
    mask = list()
    mask[0:sequence_length] = source_sequence[-sequence_length:]
    #generate the seek sequence
    seek = list()
    seek[0:len(source_sequence)-sequence_length] = source_sequence[0:len(source_sequence)-sequence_length]

    #print(mask)
    #print(seek)
    #check if mask is inside seek
    index = seq_in_seq(mask, seek)
    if (index >= 0):
        print('found sequence:', mask)
        print('in sequence: ', seek)
        print('at index: ', index)
        return True    

    return False

## see if a sub sequence is inside a master sequence. return index of repeat if any
#
def seq_in_seq(subseq, seq):
    while subseq[0] in seq:
        index = seq.index(subseq[0])
        if subseq == seq[index:index + len(subseq)]:
            return index
        else:
            seq = seq[index + 1:]
    else:
        return -1

## main
def main():
    #make sure the seed is the same for all
    lib_random.seed(42)
    
    #test submodule
    #print(is_repeat( [5, 7, 3, 5, 7] , 2 ))

    sequence_length = measure_repeat( 0, 100, 4 )
    print('', sequence_length)

    pass

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    main()