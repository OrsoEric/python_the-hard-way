#get an input string and return if it's palindroma

def is_palindrome( source ):
    source = source.casefold()

    #check if length is not EVEN
    source_len = len(source)
    #if source is not even
    if source_len % 2 != 0:
        print(source, False)
        return False

    #check if characters are the same
    for index in range(source_len//2):
        if (source[index] != source[-index -1]):
            print(source, False)
            return False

    print(source, True)
    return True

def is_palindrome_v2( source ):
    #build a string that is all small letter and eat spaces
    str_temp = source.casefold().replace(' ', '')
    #check the string with a flipped version of the string
    return [str_temp, (str_temp[:] == str_temp[::-1])]

test_vector = 
[

    
]


is_palindrome_v2( "Anna" )
is_palindrome_v2( "Maria" )
is_palindrome_v2( "2002" )
is_palindrome_v2( "Shaka" )
is_palindrome_v2( "2020" )
is_palindrome_v2( "20200202" )
is_palindrome_v2( "Angela Lava La Legna" )


