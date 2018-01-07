"""
- Implement a function, called count_vowels(str), which returns the count of all vowels in the string str. Count
uppercase vowels as well! The English vowels are "aeiouy".


- Implement a function, called count_consonants(str), which returns the count of all consonants in the string str.
Count uppercase consonants as well! The English consonants are "bcdfghjklmnpqrstvwxz".
"""


import re

VOWELS = {'a', 'e', 'i', 'o', 'u', 'y'}


def count_vowels(string):
    return len([char for char in string if char in VOWELS])


def count_consonants(string):
    return len([char for char in ''.join(re.findall('[a-zA-Z]+', string)) if char not in VOWELS])


def main():
    string = input(
        'Enter a string to get the count of vowels and consonants in it: ')
    print('Vowels count: ', count_vowels(string))
    print('Consonants count: ', count_consonants(string))


if __name__ == '__main__':
    main()
