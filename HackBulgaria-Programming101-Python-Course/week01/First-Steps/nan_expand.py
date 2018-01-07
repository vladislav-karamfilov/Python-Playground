"""
- In most programming languages, NaN stands for Not a Number.

If we take a look at the following JavaScript code:
typeof NaN === 'number' // true

We will see that in JavaScript, NaN stands for Not a NaN, which is recursive by nature.

Implement a Python function, called "nan_expand(times)", which returns the expansion of NaN (In JavaScript terms :P)
that many times.

For example:
-- If we expand NaN once (times=1), we will have "Not a NaN"
-- If we expand NaN twice (times=2), we will have "Not a Not a NaN"
-- If times=3, we have "Not a Not a Not a NaN"
-- And so on...


- Implement a function, called "iterations_of_nan_expand(expanded)" that takes a string expanded, which is an unknown
iteration of NaN Expand (check the problem for more information). The function should return the number of iterations
that have been made, in order to get to expanded. For example, if we have "Not a Not a Not a NaN" - this is the 3rd
iteration of NaN. If expanded is not a valid NaN expand string, the function should return false!
"""


def nan_expand(times):
    if times < 0:
        raise ValueError('NaN cannot be expanded negative times')

    if times == 0:
        return ''

    return ''.join(['Not a ' for _ in range(times)]) + 'NaN'


def iterations_of_nan_expand(expanded):
    count = expanded.count('Not a ')
    if nan_expand(count) == expanded:
        return count

    return False


def main():
    print('Prints the expansion of NaN')
    times = int(input('Enter how many times to expand NaN: '))
    print(nan_expand(times))
    print('\n')
    print('Gets the number of iterations of NaN expand')
    print(iterations_of_nan_expand(''))
    print(iterations_of_nan_expand('Not a NaN'))
    print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
    print(iterations_of_nan_expand("Show these people!"))


if __name__ == '__main__':
    main()
