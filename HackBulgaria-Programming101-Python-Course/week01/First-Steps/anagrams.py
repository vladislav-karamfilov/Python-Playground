"""
For anagrams check here - https://en.wikipedia.org/wiki/Anagram

For example, listen and silent are anagrams.

Implement a function is_anagram(a, b) which returns True, if the string a is an anagram of b.

Consider lowering the case of the two words since the case does not matter. SILENT and listen are also anagrams.
"""

import re


def is_anagram(original_string, other_string):
    original_letters = sorted(''.join(re.findall('[a-z]+', original_string.lower())))
    other_letters = sorted(''.join(re.findall('[a-z]+', other_string.lower())))

    return original_letters == other_letters


def main():
    print('***Anagrams check***')
    original = input('Enter the original word or phrase: ')
    other = input('Enter the other word or phrase to check for anagram: ')
    print(is_anagram(original, other))


if __name__ == '__main__':
    main()
