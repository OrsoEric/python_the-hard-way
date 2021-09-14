import time

from numpy.core.shape_base import stack, vstack

#numpy
timestamp = time.perf_counter()
import numpy as np
print(f'took {time.perf_counter() -timestamp}s to import numpy')

#excel for programmers
#import pandas

#----------------------------------------------------
#   numpy has multidimensional matrix. it's a low level fast implementation
#   rank: number of dimensions
#   shape: dimension of the matrix
#   note:
#   (9) it's just to give priority to the token
#   (9,) the coma forces recognition as a tuple token and represent a tuple of one element
#   fewest lines faster code bcause use more np builtin and less python

def test_np_constants():
    print(f"Pi: {np.pi}")

##
#
def test_np_array():
    timestamp = time.perf_counter()
    my_np_array = np.array( [x for x in range(0, 10)] )
    print(f'took {time.perf_counter() -timestamp}s to execute')
    print('construct a 1D array using list comprhension')
    print(f'content: {my_np_array}')
    print(f'type: {my_np_array.dtype} | dimensions: {my_np_array.ndim} | shape: {my_np_array.shape}')
    print(f' access element: {my_np_array[0]}')
##
#
def test_np_matrix():
    my_np_matrix = np.array( [[y for y in range(0,3) ]  for x in range(0, 5) ]  )
    print('construct a 2D matrix using list comprhension')
    print(f'content: {my_np_matrix}')
    print(f'type: {my_np_matrix.dtype} | dimensions: {my_np_matrix.ndim} | shape: {my_np_matrix.shape}')
    print(f' access element: {my_np_matrix[0][0]}')
    print(f' access element with numpy overloaded access: {my_np_matrix[0,0]}')
    print(f' access row: {my_np_matrix[0]}')

## 
#
def test_change_shape():
    my_np_matrix = np.array( [[y for y in range(0,6) ]  for x in range(0, 10) ]  )
    print('reshape a matrix after creation')
    print(f'content: {my_np_matrix}')
    print(f'type: {my_np_matrix.dtype} | dimensions: {my_np_matrix.ndim} | shape: {my_np_matrix.shape}')
    #internally this assignment calls a setter in the np class
    my_np_matrix.shape = (3,20)
    print(f'content: {my_np_matrix}')
    print(f'type: {my_np_matrix.dtype} | dimensions: {my_np_matrix.ndim} | shape: {my_np_matrix.shape}')
    #reshape in a way that makes sense
    my_np_matrix.reshape(3, -1)
    print(f'convert to 1D: {my_np_matrix.ravel()}')
    

def test_create_array():
    print(f"linspace (divide in #points): {np.linspace(0,10, 15)}")
    print(f"arange: (set separation){np.arange(0.0,10.0, 0.5)}")
    print(f"eye: {np.eye(3)}")    
    print(f"zeros: {np.zeros((3,2))}")    
    print(f"ones: {np.ones((4,3))}")
    print(f"full: {np.full((4,3), dtype=float, fill_value=0.090)}")
    print(f"empty, allocate without initiaize: {np.empty}")
    print(f"random: {np.random.random((5,5))}")
    print(f"transpose: {np.random.random((5,5)).T}")


def test_concatenate():
    #build 10x10 of zeros and a core 6x6 of ones
    #stack horizontally zero, one, zero at the center
    middle = np.block( [ np.zeros((6, 2)),np.ones((6,6)), np.zeros((6, 2))]  )
    #stack zero one zero vertically
    result = np.block( [[np.zeros((2, 10))], [middle], [np.zeros((2, 10))]]  )
    print(f"result {result}| shape {result.shape}")


def test_txt():
    my_2d_array = np.random.random((10,10))
    np.savetxt("xxx.txt",my_2d_array)
    result = np.loadtxt("xxx.txt")
    print(f"source matrix {my_2d_array}")
    print(f"saved and reloaded in txt {result}")

def test_indexing():
    print("numpy redefine how square brackets work")
    #construct a matrix. count a 1D array and reshape
    my_2d_array = np.array(range(100))
    my_2d_array = my_2d_array.reshape((10,-1))
    print(my_2d_array)
    print(f"take a sub matrix by np overloaded range access: {my_2d_array[2:6, 3:7]}")
    print(f"invert the order of the elements: {my_2d_array[::-1]}")
    print(f"i can use an array to reorder another array: {my_2d_array[[(9,5), (7,5)]]}")
    
    print("use np indexing to build 10x10 of zeros and a core 6x6 of ones")
    my_2d_array = np.zeros((10,10))
    my_2d_array[2:8, 2:8] = 1.0
    print(my_2d_array)
    #this is complex as the operator act backward as a LHR to overload
    print(f"complex subtract 0.5-np.array: {0.5 -my_2d_array}")

    print(f"modulus operator on an array: {np.array([x for x in range(0, 10)]) % 3}")
    
## Broadcasting
#   arrays are extended along other axis to have compatile shapes
def test_broadcast():
    #create an array of 100 elements and change 1D to 3D
    my_array_a = np.array(range(100)).reshape(2, 5, -1)
    #my_array_b = np.ones((10,10))
    print(f"multiply by scalar {2.0 * my_array_a}")
    my_array_b = np.array(range(0,10))
    result = my_array_a *my_array_b
    print(f"multiply by 1D {my_array_a.shape} {my_array_b.shape} | result\n {result} {result.shape}")

##
#
def test_copy():
    #create origin
    my_array_a = np.array(range(10)).reshape(2, -1)
    #create view and copy
    #my_array_view = my_array_a.view(my_array_a)
    #my_array_copy = my_array_a.copy(my_array_a)
    
    #my_array_copy[1,1] = -100
    #print(f"modify copy does not modify view {my_array_copy} -> {my_array_a}")
    #my_array_view[1,1] = -100
    #print(f"modify copy does not modify view {my_array_view} -> {my_array_a}")

    
    #astype changes the type

    my_array = np.linspace(1.0, 10.0, 20)
    my_array_int = my_array.astype( int )
    print(f"{my_array} {my_array_int}")

def test_operators():
    my_array = np.random.random((5,5))
    print(f"source\n {my_array}")
    print(f"matrix multiplication\n {my_array@my_array}")
    print(f"exp operator is element by element\n {np.exp(my_array)}")
    print(f"multiplication element by element\n {my_array * my_array}")
    print(f"sum of all elements\n {my_array.sum()}")
    print(f"sum of all elements along axis 0\n {my_array.sum(axis=0)}")
    print(f"sum of all elements along axis 1\n {my_array.sum(axis=1)}")









#test_np_constants()
#test_np_array()
#test_np_matrix()
#test_change_shape()
#test_create_array()
#test_create_array()
#test_concatenate()
#test_txt()
#test_indexing()
#test_broadcast()
#test_copy()
test_operators()