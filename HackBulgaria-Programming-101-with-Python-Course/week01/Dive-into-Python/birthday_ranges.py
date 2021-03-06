"""
Implement a function birthday_ranges(birthdays, ranges) We have a list birthdays and list of tuples ranges.
birthdays - range from 0 to 365, ranges - ranges (one range is a tuple of two numbers - start and end.

We want to calculate, for each tuple, how many people are born in that range (between start and end inclusive).

For example:
Birthdays - [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15]
Ranges - [(4, 9), (6, 7), (200, 225), (300, 365)]

Will give the result:
[5, 2, 0, 1]
As we can see, between 4 and 9, inclusive, there are 5 people with birthdays - 5, 6, 7, 4, 5. Between 300 and 365
there is exactly one birthday - 300.
"""


def birthday_ranges(birthdays, ranges):
    result = [0 for _ in ranges]

    for i, current_range in enumerate(ranges):
        for current in range(current_range[0], current_range[1] + 1):
            result[i] += birthdays.count(current)

    return result


def main():
    print('***Check how many birthdays in a list of birthdays are in specific ranges***')
    print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
    print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))


if __name__ == '__main__':
    main()
