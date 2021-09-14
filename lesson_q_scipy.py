import time

#numpy
timestamp = time.perf_counter()
import numpy as np
print(f'took {time.perf_counter() -timestamp}s to import numpy')

#scipy
timestamp = time.perf_counter()
import scipy as lib_scipy
print(f'took {time.perf_counter() -timestamp}s to import scipy')

##
#   good implementation for sparse matricies with lots of zeros
from scipy import sparse

def test_sparse():
    my_mat = sparse.lil_matrix((int(1e6), int(1e6)))
    print(f"{my_mat.shape}")
    my_mat[5e3, 5e3] = 42
    #print(f"{a in (my_mat.shape >0)}")

test_sparse()