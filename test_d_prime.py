## prime factor
# function that return the prime factors

def factorize( my_source : int ) -> list():
    #make int
    num = int(my_source)
    #initialize factor list
    my_factors = list()
    #init while
    div = 2
    while div <= num:
        #if: I found a factor
        if (num % div) == 0:
            #print(num % div, num, div)
            #divide by the factor
            num //= div
            #print(num)
            #add factor to the list
            my_factors.append(div)

        #if divisor is no factor
        else:
            #advance to next divisor
            div+=1
    
    #if no factors were found
    if not my_factors:
        #put the original number in the list of factors
        my_factors.append(num)

    print(my_source, my_factors)
    return my_factors

def main():
    factorize(1)
    factorize(42)
    factorize(100)
    factorize(13)
    factorize(10000)
    factorize(9999)
    factorize(128)
    factorize(112587)

    return None

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    main()