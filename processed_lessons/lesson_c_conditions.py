##  LOOPS
#   in python aim should be to use high level loop construct and avoid c style nested for/while loops



def test_if():
    print("-------------------------------")
    print("\tif")

    if True:
        print(f'if checks a boolean condition')
    
    if all( [True, True, True] ):
        print(f'all() is a wired and')

    list_small = ["red", "grey"]
    list_big = ["red", "green", "blue", "grey", "white"]

    if all(item in list_big for item in list_small):
        print(f'all can be combined with for scan in iterable to make 2D scans')


test_if()