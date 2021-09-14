## matrix 10x10 of random numbers. normalize so that the sum along the rows is 1
#used to log
import logging
import time
import math
import numpy as lib_numpy

SOURCE_ROWS = 3
SOURCE_COLS = 5

def excercise():
    #build matrix
    my_mat = lib_numpy.random.random((SOURCE_ROWS, SOURCE_COLS))
    #my_mat = lib_numpy.full((SOURCE_ROWS, SOURCE_COLS), fill_value=2.0)
    logging.debug(f"source:\n {my_mat}")

    my_mat_sum = my_mat.sum(axis=1)
    logging.debug(f"sum of rows: {my_mat_sum}")

    for row in range(my_mat.shape[0]):
        logging.debug(f"divide row {row} by {my_mat_sum[row]}")
        my_mat[row,:] /= my_mat_sum[row]

    logging.debug(f"result:\n {my_mat}")
    logging.debug(f"sum of rows: {my_mat.sum(axis=1)}")


def excercise_prof():
    my_mat = lib_numpy.random.randint(0, 10+1, (SOURCE_ROWS, SOURCE_COLS))
    logging.debug(f"source:\n {my_mat}")
    logging.debug(f"sum of rows:\n {my_mat.sum(axis=1, keepdims=True)}")

    #division element by element broadcasting right size of the matrix and using sum to refactor
    return_mat = my_mat / my_mat.sum(axis=1, keepdims=True)
    logging.debug(f"result:\n {return_mat}")
    logging.debug(f"sum of rows:\n {return_mat.sum(axis=1, keepdims=True)}")
    #assert if condition is false
    assert all(math.isclose(x,1) for x in return_mat.sum(axis=1)), "ERR"
    #lib_numpy.sum(  , axis =0 )


import logging
import numpy as lib_numpy

NUM_ATHLETES = 5
NUM_JUDGES = 10
MIN_VOTE = 1
MAX_VOTE = 10

def exercise2():
    #matrix of votes 10 judges 5 athletes
    #remove the lowest and highest votes
    #compute average
    vote_matrix = lib_numpy.random.randint(MIN_VOTE, MAX_VOTE+1, (NUM_ATHLETES, NUM_JUDGES))
    logging.info(f"votes:\n {vote_matrix}")
    #sort the values along the rows, with the lowest value on compun 0 and the highest value on the last column
    sorted_vote_matrix = lib_numpy.sort(vote_matrix, axis=1)
    logging.debug(f"sort:\n {sorted_vote_matrix}")
    #eliminate the first and last column. this excludes the highest and lowest vote
    reduced_vote_matrix = sorted_vote_matrix[ :, 1:NUM_JUDGES-1 ]
    logging.debug(f"reduced:\n {reduced_vote_matrix}")
    #compute the mean of each rows
    score_matrix = reduced_vote_matrix.mean(axis=1,keepdims=True)
    logging.info(f"average:\n {score_matrix}")
    
def exercise2_alssandro_censi():
    voti = lib_numpy.random.randint(1, 11, size=(5,10))
    print(voti)
    print("\n")
    somme = voti.sum(axis=1, keepdims=1) - lib_numpy.max(voti, axis=1, keepdims=1) - lib_numpy.min(voti, axis=1, keepdims=1)
    medie = somme / (voti.shape[1]-2)
    print(somme)
    print("\n")
    print(medie)

def main():
    #excercise()
    #excercise_prof()
    exercise2()
    pass

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        #level=logging.INFO,
        level=logging.DEBUG,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()

