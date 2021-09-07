##  Data Structures
#   LHR = RHS
#       C
#   In C LHR is a memory point to a place in memory, RHS is a value
#   e.g.
#   a = 5; //in memory, a piece of memory four byte longs starting from 0x04ac will contain the S32 number 5
#       Python
#   In Python LHR is a tag/name, RHS is an object in memory
#   e.g.
#   a = 5
#   b = 5
#   the object 5 is created in memory. the tags 'a' and 'b' both point to this object. When an object in memory is not pointed by any tag, the garbage collector destoy it
#
#       Object Attributes
#   immutable       : object that cannot change once created. e.g. the number 5 is immutable.
#   mutable         : the object pointed by the tag can be changed
#
#   heterogeneus    : object can hold many types of object at once
#   homogeneus      : object can hold just one type of object  
#       

##  Bytearray
#   Used to represent unicodes characters, that may need more thann one byte
def test_bytearray():
    print("-------------------------------")
    print("\tbytearray()")
    my_byte_array = bytearray([0x42, 0x24])
    print(f'bytearray: {my_byte_array}')

##  List
#   mutable, heterogeneus
def test_list():
    print("-------------------------------")
    print("\tlist()")
    #construct an empty list
    my_list = list()
    #list can hold many types of objects, including other lists
    my_list.append( 'a' )
    my_list.append( 3 )
    my_list.append( [4,5] )
    print(f"list is homogeneus: {my_list}")
    #object in a list can be changed
    my_list[1] = 'shaka'
    print(f"list is mutable: {my_list}")
    #python is shallow. two list are the same
    my_list_shallow = my_list
    my_list_shallow[0] = -99.0
    print(f"shallow assignment: changing my_list_shallow {my_list_shallow} changes my_list {my_list}")
    #remove an object from a list
    my_list_shallow.remove( my_list_shallow[1] )
    print(f"remove element: my_list_shallow {my_list_shallow} | my_list {my_list}")
    #list can be concatenated
    my_concatenated_list = my_list +['con', 'cat', 'enated']
    print(f"list can be concatenated with '+' {my_concatenated_list}")

    return

##  Tuple
#   immutable, heterogeneus
def test_tuple():
    print("-------------------------------")
    print("\ttuple()")
    my_tuple = tuple( (1, 'shaka', -3.33) )
    print(f"tuple are immutable, heterogeneus: {my_tuple}")

    return

##  String
#   immutable, homogeneus
def test_string():
    print("-------------------------------")
    print("\tstr()")

    print(f'str() are immutable, homogeneus: {"shaka"}')

    #the single apex allow to remove escape sequence on double apex
    str_a = "hi \"Doc\"!"
    str_b = 'hi "Doc"!'
    print(f"strings are defined with either single and double apex: <{str_a}> <{str_b}> ")

    return



##Execute tests
test_bytearray()
test_list()
test_tuple()
test_string()
