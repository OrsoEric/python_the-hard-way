## @package pyexample
#  Documentation for this module.
#
#  More details.
 
## Test print
#   Test optional arguments of print
def f_test_print():
    #print
    print("Shaka", 23, 10)
    #custom separator. default is a space " "
    print("Shaka", 23, 10, sep='|')
    #print on another stream
    import sys
    print("Shaka", file=sys.stderr )

f_test_print()

