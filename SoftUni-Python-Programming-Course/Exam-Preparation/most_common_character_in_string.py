# Problem description: http://python3.softuni.bg/student/lecture/assignment/56b5f1b37e4f59b649b7e611/

import operator


def get_most_common_character_in_string(string):
    if not string or string.isspace():
        return 'INVALID INPUT'

    char_occurrences = {}
    for char in string:
        if char in char_occurrences:
            char_occurrences[char] += 1
        else:
            char_occurrences[char] = 1

    most_common_char = max(char_occurrences.items(),
                           key=operator.itemgetter(1))[0]
    return most_common_char


def main():
    print(get_most_common_character_in_string(input()))


if __name__ == '__main__':
    main()
