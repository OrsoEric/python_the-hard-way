#import pandas as lib_pandas
#import numpy as lib_numpy

print("Hello World");

#lib_numpy.array;


#a = lib_pandas.UInt16Dtype();
#print(a);

a= 2**2281-1;
print(a);

a = 23;
if a==23:
    print("woah!!!");
    a = a/2;
print(a);

id_a = id(a);
print(id_a);

"""
shaka multi line comment.
can work as code documentation
"""

#assign a label to the number 42
foo = 42;
#compute 42+1 and move the label to the new number 43
foo = foo+1;
print(foo);

#unicode
my_string = "42"
bar = (4,2)
byte_array = bytearray([0x42, 0x24]);


#tupla ()
#stringa []

#set
my_set = { 3, 7 };
my_set = frozenset( { 3, 7 } );
#maps: assign a lable to each value
my_set_map = { "shaka" : 42, "fell" : 43 };
print(my_set_map);

#No type object. similar to null pointer
foo = None;

#An input will ask on console with .py and will ask with a dialog on top with .ipynb
#my_input = input("xxx")
#print()

#for loop and : indent is enforced
for n in range(5):
    print("row: ", n)

#Constructors for default types
my_int = int()
my_string = str(42)
print(my_int, my_string)

#all should point to the same object 1 with different lables
#https://pythontutor.com/
my_int = 1
my_int_b = int(1)
my_int_c = int("1")
MY_FLOAT = 1.0
my_float = float(1.0)

## Test print
#   Test optional arguments of print
def test_division( num, div ):
    #Operators. The / is float division. the // is integer division
    a = num / div
    b = num // div
    print( a, b )

test_division(7, 2)

#-----------------------------------------------------------------

## Test print
#   Test optional arguments of print
def test_module( num, div ):
    ret = num % div
    print("module: ", num, div, ret)
    return ret

test_module( 7, 2 )
#module is defined for floating points ???
test_module( 3.5, 0.8 )

#-----------------------------------------------------------------

## Test increment
#   post increment doesn't exist because numbers can't change
def test_increment( cnt ):
    #cnt++
    cnt += 1
    cnt = cnt + 1
    return cnt

print( "increment: ", test_increment( 10 ) ) 

#-----------------------------------------------------------------

def test_operator_tilda( num ):
    ret = ~num
    print( "not", num, ret )
    return ret

test_operator_tilda( 10 )
#not defined for non integer
#test_operator_tilda( 3.87 )
#test_operator_tilda("ciao")

#-----------------------------------------------------------------

#   [] list: mutable, heterogeneus
#   () tuple: non mutable, heterogeneous
#   "" string: non mutable, homogenous

## Test sequences
#   ordered. i can iterate
#   list: mutable, heterogeneus
my_list = [28.1, 28., 28.5, 29]
print( type(my_list), "| ", my_list[0], "| ", my_list )

#sequences can be concatenated
#list can have many types
my_list = my_list + ["shaka" , 0, 3+4j]
print( type(my_list), "| ", my_list )

#create a string from a list using constructor. it translates everything into chars
my_string = str( my_list )
print( type(my_string), "| ", my_string[0], "| ", my_string )

#-----------------------------------------------------------------

#operators on sequence
if 28.1 in my_list:
    print("sequence check pass")
else:
    print("sequence check not pass")

#concatenate repeat list
print("repeat a list: ", my_list *3 ) 
#repeat operator
#print("shaka" *"wall")

#-----------------------------------------------------------------

#generate a sequence of count
my_sequence = []
for cnt in range(10):
    my_sequence = my_sequence +[(cnt +1)]
print( "generate count sequence", my_sequence )
#I can slice a sequence. negative is counted from the end
print("first and last element", my_sequence[0], my_sequence[-1] )
print("slice a sequence", my_sequence[3:6]  )
#-3 from the end
print("slice a sequence", my_sequence[3:-3]  )

#implicit index
print("slice a sequence", my_sequence[:6]  )
print("slice a sequence", my_sequence[3:]  )
print("slice a sequence", my_sequence[:]  )
print("slice a sequence", my_sequence[::1]  )
#allows to skip a number of elements
print("slice a sequence", my_sequence[::2]  )
#reverse sequence
print("slice a sequence", my_sequence[::-1]  )

start = 3
end = 7
skip = 2
print("slice a sequence", my_sequence[start:end:skip]  )

print("len of the sequence", len(my_sequence) )

#-----------------------------------------------------------------

#Assignment is reference
my_sequence_b = my_sequence
my_sequence_b[1] = -1000
print("asignment is reference", my_sequence_b[1], my_sequence[1])

#-----------------------------------------------------------------

print("type of range", type(range(10)) )

#for with range
my_sequence = []
start = 3
end = 13
skip = 2
for cnt in range(start, end, skip):
    my_sequence = my_sequence +[cnt]
print("range is used to generate sequences of integer", type(my_sequence), my_sequence)

#range can be used to sequence elements
for cnt in range(len(my_sequence)):
    my_sequence[cnt] = 0
print("iterate with range on list",my_sequence)

#-----------------------------------------------------------------

my_sequence_b = []
for index, value in enumerate( my_sequence ):
    my_sequence_b += [index, value]
print(" enumerate is used to extract both index and value from a sequence", my_sequence_b)

my_sequence_b = []
for x in enumerate( "ciao"):
    my_sequence_b += [x]
print("enumerate generate a touple", my_sequence_b)


#-----------------------------------------------------------------

#Three types of for

#have value
for value in my_sequence :
    value = value

for index in range(len(my_sequence)):
    index = index

#have both index and value
for index, value in enumerate( my_sequence ):
    index = index
    value = value

#-----------------------------------------------------------------

my_sequence = []
#zip allow to iterate over a sequence of sequence
for a, b in zip("shaka", "piazza"):
    my_sequence += [(a, b)]
print("zip allow to take elements from multiple sources", my_sequence)

#-----------------------------------------------------------------

#touple

my_sequence = ()
for cnt in range(3, 9):
    #my_sequence = my_sequence +(cnt)
    cnt
print("generate touple", type(my_sequence), my_sequence)

#-----------------------------------------------------------------

#sort
birthday = [ ("Homer", 1400), ("Columbus", 1000), ("Emperor", 40000), ("Euler", -2000) ]
print("unsorted: ", birthday)
birthday.sort()
print("sorted only by first element of the tuple: ", birthday)
#sorted generate a new sequence
print("sort reverse order: ", sorted(birthday, reverse=True))

#-----------------------------------------------------------------

seq_a = [1,2,3,4]
seq_b = ["a","b","c"]
print(seq_a, seq_b)
seq_a[1:3] = seq_b
print("I can assign slices on the LHS while changing length", seq_a, seq_b)

#-----------------------------------------------------------------

seq_b = seq_a
#assign tag to an empty sequence doesn't delete elements
#seq_a = [] 
#delete the elements of the list. include other tagged references
seq_a .clear()
print("delete elements", seq_a, seq_b)

#-----------------------------------------------------------------

check_sequence = [ True, False, False, False, True ]
print(check_sequence, "| any: ", any(check_sequence), "| all: ", all(check_sequence) )


#-----------------------------------------------------------------

#the single apex allow to remove escape sequence on double apex
str_a = "hi \"Doc\"!"
str_b = 'hi "Doc"!'
print("strings", str_a, str_b )

#-----------------------------------------------------------------

#f strings allow to generate formatted strings without fiddling with concatenation
answer = 42
print("f-string", f"the answer is: {answer}!!! ")

#-----------------------------------------------------------------

#split strings along spaces. I can use the split method from both the string class of from the string object
str_a = "Shaka  When The\tWalls Fell"
str_b = str.split( str_a )
str_b = str_a.split()
print("split along white:", type(str_a), str_a, type(str_b), str_b )
str_b = str_a.split(' ')
print("split along single space:", type(str_b), str_b )

#-----------------------------------------------------------------

str_a = "Giovannini"
print("join applied to list to string:", str_a, "|".join(list(str_a)))

str_a = "Shaka  When The\tWalls Fell"
str_a = str_a.split()
str_b = str.join("+",str_a)
print("Use join to replace white spaces with +: ", str_b)

#-----------------------------------------------------------------

#Make small case. german beta is SS. 
str_a = "DiE GrOße"
print("use casefold to make small: ",str_a,str_a.casefold() )

#-----------------------------------------------------------------
