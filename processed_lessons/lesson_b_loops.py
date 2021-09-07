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

    return


test_for()