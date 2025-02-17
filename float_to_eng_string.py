#used to log
import logging

##  Generate engineering format string
#   the conversion is not done using the builting number to string function, due to the need to exactly control digits sign and separator
#   
def float_to_eng_string(source : float, significant_digits : int= 4  ) -> str() :
     
    #----------------------------------------------------
    #   sign correction
    #----------------------------------------------------

    if (source >= 0.0):
        value = source
        output_str = "+"
    else:
        value = -source
        output_str = "-"
    logging.debug(f'source: {source} | value: {value} | output string: {output_str}')

    #----------------------------------------------------
    #   exponent detection and normalization
    #----------------------------------------------------

    #make sure number is between 1.0 and 1000.0
    exp_index = 0
    while True:
        logging.debug(f'normalization | value: {value} | exponent: {exp_index}')
        #if underflow
        if (exp_index <= -6):
            output_str += "0.000 "
            logging.debug(f'underflow | value: {value} | exponent: {exp_index}')
            return output_str

        #if overflow
        elif (exp_index >= 6):
            output_str += "INF   "
            logging.debug(f'overflow | value: {value} | exponent: {exp_index}')
            return output_str

        #if too small
        if (value < 1.0):
            #inflate by 1000X
            value *= 1000.0
            exp_index -= 1
            logging.debug(f'shrink | value: {value} | exponent: {exp_index}')

        #if too big
        elif (value > 1000.0):
            #deflate by 1000X
            value /= 1000.0
            exp_index += 1
            logging.debug(f'inflate | value: {value} | exponent: {exp_index}')

        #sweet spot
        else:
            x_done = False
            #n_margin = (50)/(10**significant_digits)
            #logging.debug(f"margin: {n_margin}")
            #scan the three possible bases after normalization
            for base in [100.0, 10.0, 1.0]:
                #if the value is within the scan limit
                if (value >= base):
                        x_done = True
                        logging.debug(f"normalization complete | value: {value} | base: {base}")
                        break
                #if the value is below scan limit
                else:
                    #scan a smaller base
                    pass
            #the renormalization is complete
            if x_done == True:
                #done renormalizing
                break
    
    #----------------------------------------------------
    #   digit computation and decimal separator
    #----------------------------------------------------

    #for digit_index in range( 0, significant_digits ):
    digit_index = 0
    while True:
        logging.debug(f'digit processing | value: {value} | base: {base} | index: {digit_index}')
        #if the base is big enough
        if (value >= base):
            #the last digit needs to be rounded
            if (digit_index >= significant_digits -1):
                #compute digit
                digit_int = round(value / base)
                #if the rounding would push the number 
                #if digit_int >= 10:
                logging.debug(f'last digit rounding | value: {value} | base: {base} | digit: {digit_int} | index: {digit_index}')

            #core digits do not need rounding
            else:
                #compute digit
                digit_int = int(value // base)
                logging.debug(f'digit computed | value: {value} | base: {base} | digit: {digit_int} | index: {digit_index}')

            #add the digit to the string
            if ((digit_int < 0) or (digit_int > 9)):
                #re-execute by rounding now that I know that I must round
                value = source +(10**(3*exp_index))*(50)/(10**significant_digits)
                logging.debug(f'rounding detected! | {exp_index} {(10**(3*exp_index))*(50)/(10**significant_digits)} | value: {source} ->  base: {value}')
                return float_to_eng_string(value, significant_digits  )

            output_str += f"{digit_int}"
            digit_index += 1
            #if value is reduced below unity, i need to place a point
            if (base == 1.0):
                output_str += "."
                logging.debug(f'add decimal separator | value {value} | up: {10.0 +(5.0)/(10**significant_digits)} | down: {1.0 -(0.5)/(10**significant_digits)} | string {output_str}')
            #update base and value
            value -= base *digit_int
            base /= 10.0
            logging.debug(f'processing... | value: {value} | base: {base} | string: {output_str}')

        #if base is small
        elif (base > value):
            #update base
            base /= 10.0
            #i have yet to start processing digits
            if (digit_index == 0):
                logging.debug(f'blank non significant digit | value: {value} | base: {base}')
                #do nothing
                pass
            #if i'm processing digits
            else:
                #add a zero
                output_str += "0"
                digit_index += 1
                logging.debug(f'digit computed | value: {value} | base: {base} | digit: {0} | index: {digit_index}, string: {output_str}')
                #if base falls at 1.0
                if (base == 0.1):
                    output_str += "."
                    logging.debug(f'add decimal separator | base {base} | string {output_str}')
                else:
                    pass

        #if i printed enough digits
        if (digit_index >= significant_digits):
            logging.debug(f'enough digits have been processed | {digit_index} of {significant_digits}')
            #done
            break

        assert not (value < 0.0), f"negative! {value}"    

    #----------------------------------------------------
    #   SI sign and return
    #----------------------------------------------------

    #now append the S.I. modifier
    si_suffix = "afpnum KMGTPE"
    output_str += si_suffix[6 +exp_index]
    logging.debug(f'result: {output_str}')
    return output_str
