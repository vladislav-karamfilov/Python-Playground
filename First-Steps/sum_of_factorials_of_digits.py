"""
Implement a function fact_digits(n), that takes an integer and returns the sum of the factorials of each digit of n.

For example, if n = 145, we want 1! + 4! + 5!
"""


from math import factorial


def fact_digits(n):
    if n < 0:
        n = -n

    sum_of_factorials = 0
    while n != 0:
        sum_of_factorials += factorial(n % 10)
        n //= 10

    return sum_of_factorials


def main():
    n = int(input('Enter a number to get the sum of the factorials of its digits: '))
    sum_of_factorials = fact_digits(n)
    print(sum_of_factorials)

if __name__ == '__main__':
    main()
