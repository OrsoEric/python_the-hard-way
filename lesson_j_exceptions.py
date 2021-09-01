#-------------------------------------------------------------------
#-----------------------------------------------
#   I use exception to catch a division by zero

#
import random
from warnings import catch_warnings

# raise raise an exception


def risky_operation():
    while True:
        num = random.randint(0, 100)
        num = 100 /num
        print("OK: ", num)
        
    return None

try:
    risky_operation()
except ArithmeticError as problem:
    print(problem)


#-----------------------------------------------
#   assert
#   will check the obvious. will be disabled in production. python -O -OO removes them



#-----------------------------------------------
#   IO
#   keyword 'with' 'as'
#   used with an object that is capable of releasing itself
# this program will copy an input in output

try:
    with open('input.txt', 'r') as my_input, open('output.txt', 'w') as my_output:
        for line in my_input:
            my_output.write(line)
except OSError as problem:
    print('problem', problem)

