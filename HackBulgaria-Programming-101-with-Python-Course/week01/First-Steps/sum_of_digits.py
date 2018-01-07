"""
Given an integer, implement a function, called sum_of_digits(n) that calculates the sum of n's digits.

If a negative number is given, our function should work as if it was positive.

Keep in mind that in Python, there is a special operator for integer division!
"""


def sum_of_digits(n):
    if n < 0:
        n = -n

    result = 0
    while n != 0:
        result += n % 10
        n //= 10

    return result


def main():
    n = int(input('Enter a number to get the sum of its digits: '))
    print(sum_of_digits(n))

    # print(sum_of_digits(1325132435356))
    # print(sum_of_digits(123))
    # print(sum_of_digits(6))
    # print(sum_of_digits(-10))


if __name__ == '__main__':
    main()
