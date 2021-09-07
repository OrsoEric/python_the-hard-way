##  Generate engineering format string
#   
#   

def float_to_eng_string(source : float, significant_digits : int= 4  ) -> str() :
     
    #sign correction
    if (source >= 0.0):
        value = source
        output_str = "+"
    else:
        value = -source
        output_str = "-"

    #make sure number is between 1.0 and 1000.0
    exp_index = 0
    while True:
        #if underflow
        if (exp_index <= -6):
            output_str += "0.000 "
            return output_str

        #if overflow
        elif (exp_index >= 6):
            output_str += "INF   "
            return output_str

        #if too small
        if (value < 1.0):
            #inflate by 1000X
            value *= 1000.0
            exp_index -= 1

        #if too big
        elif (value > 1000.0):
            #deflate by 1000X
            value /= 1000.0
            exp_index -= 1

        #sweet spot
        else:
            if (value >= 100.0):
                #if would cause rounding problems
                if (value >= 1000.0 -(5*1000.0)/(10**significant_digits)):
                    value += (5*100.0)/(10**significant_digits)
                    pass
                else:
                    #sweet spot
                    break

                #initialize base
                base = 100.0
            elif (value >= 10.0):
                #initialize base
                base = 10.0
                break
            elif (value >= 1.0):
                #initialize base
                base = 1.0
                break
            else:
                pass

    
    #for digit_index in range( 0, significant_digits ):
    digit_index = 0
    while True:
        #if the base is big enough
        if (value >= base):
            #the last digit needs to be rounded
            if (digit_index >= significant_digits -1):
                #compute digit
                digit_int = round(value / base)
                #if the rounding would push the number 
                #if digit_int >= 10:

            #core digits do not need rounding
            else:
                #compute digit
                digit_int = int(value // base)


            #add the digit to the string
            output_str += f"{digit_int}"
            digit_index += 1
            
            
            #update base and value
            value -= base *digit_int
            base /= 10.0
            #if value is reduced below unity, i need to place a point
            if (value < 1.0) and (value > 0.1):
            #if (base == 1.0):
                output_str += "."
        #if base is small
        elif (base > value):
            #update base
            base /= 10.0
            #i have yet to start processing digits
            if (digit_index == 0):
                #do nothing
                pass
            #if i'm processing digits
            else:
                #add a zero
                output_str += "0"
                digit_index += 1
                #if base falls at 1.0
                if (base == 0.1):
                    output_str += "."

        
        #if i printed enough digits
        if (digit_index >= significant_digits):
            #done
            break

        assert not (value < 0.0), f"negative! {value}"    
        print(f"base: {base} | value: {value} | digit_int: {digit_int} | {output_str}")
    #now append the S.I. modifier
    si_suffix = "afpnum KMGTPE"
    output_str += si_suffix[6 +exp_index]    
    return output_str

#assert not ((digit_int < 0) or (digit_int > 9)), f"ERR {digit_int} {digit}"

#core test
#test_vector = [ 234.56 ]
test_vector = [ 999.99999 ]
#test_vector = [0.1, 0.33, 1.0, 3.34, 9.99999, 10.0, 33.412, 99.999999, 100.0, 345.6]
for value in test_vector:

    temp_str = float_to_eng_string(value)
    try:
        temp_float = float(temp_str[:-1])
    except:
        temp_float = 0.0
    if temp_str[-1] == 'm':
        temp_float /= 1000.0

    print("---------------------------------")
    print(f"Value: {value} | Eng: {temp_str} -> ERR: {value -temp_float}")
    print("---------------------------------")
