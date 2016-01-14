"""
Implement a function, called to_number(digits), which takes a list of integers -
digits and returns the number, containing those digits.
"""


def to_number(digits):
    digits_count = len(digits)
    if digits_count == 0:
        raise ValueError('Cannot convert empty list of digits to a number!')
    
    number = 0
    power = digits_count - 1
    for digit in digits:
        if digit < 0 or digit > 9:
            raise ValueError('{0} is not a digit!'.format(digit))

        number += digit * pow(10, power)
        power -= 1

    return number


def main():
    digits_string = input('Enter the digits of the number separated by comma: ')
    try:
        digits = [int(x.strip()) for x in digits_string.split(',')]
        number = to_number(digits)
        print(number)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
