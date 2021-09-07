##  LOOPS
#   in python aim should be to use high level loop construct and avoid c style nested for/while loops

def test_for():
    print("-------------------------------")
    print("\tfor in")

    print('c style loop uses range()')
    for index in range(0, 10):
        print(f'{index}|', end='')
    print('')

    print('scan any iterable container like list()')
    iterable_sequence = ['shaka', 99, [1, -99.0], 'rei']
    for item in iterable_sequence:
        print(f'{item}|', end='')
    print('')

    
    my_sequence = list()
    str_a = "shaka"
    str_b = "piazza"
    for a, b in zip(str_a, str_b):
        my_sequence += [(a, b)]
    print(f"zip() scans two iterables but ends when the shortest end: {my_sequence}")
    

    return


test_for()