"""
Implement a function, called to_digits(n), which takes an integer n and returns a list, containing the digits of n.
"""


def to_digits(n):
    if n < 0:
        n = -n
    elif n == 0:
        return [0]

    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    
    digits.reverse()
    return digits


def main():
    n = int(input('Enter a number to get a list of its digits: '))
    digits = to_digits(n)
    print(digits)


if __name__ == '__main__':
    main()
