## matrix 10x10 of random numbers. normalize so that the sum along the rows is 1
#used to log
import logging
import time
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

    lib_numpy.sum(  my_mat / my_mat.sum(axis=1, keepdims=True), axis =0 )
    logging.debug(f"result:\n {my_mat}")

def main():
    excercise()
    #excercise_prof()
    pass

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.DEBUG,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()