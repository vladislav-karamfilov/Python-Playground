"""
Implement a function called char_histogram(string) which takes a string and returns a dictionary where each key is a
character from string and its value is the number of occurrences of that char in string.
"""

from pprint import pprint as pp


def char_histogram(string):
    histogram = {}
    for char in string:
        if char in histogram.keys():
            histogram[char] += 1
        else:
            histogram[char] = 1

    return histogram


def main():
    string = input('Enter a string to get its char histogram: ')
    pp(char_histogram(string))


if __name__ == '__main__':
    main()
