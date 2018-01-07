"""
You are given a string, where there can be numbers.
Return the sum of all numbers in that string (not digits, numbers)
"""

import re


def sum_of_numbers(string):
    return sum([int(x) for x in re.findall('\d+', string)])


def main():
    print('***Gets the sum of all numbers in a given string***')
    print(sum_of_numbers("1111"))
    print(sum_of_numbers("abcd"))
    print(sum_of_numbers("1abc33xyz22"))
    print(sum_of_numbers("ab125cd3"))
    print(sum_of_numbers("ab12"))


if __name__ == '__main__':
    main()
