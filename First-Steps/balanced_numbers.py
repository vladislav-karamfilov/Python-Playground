"""
A number is called balanced, if we take the middle of it and the sums of the left and right parts are equal.

For example, the number 1238033 is balanced, because it's left part is 123 and right part is 033.

We have : 1 + 2 + 3 = 0 + 3 + 3 = 6.

A number with only one digit is always balanced!

Implement a function is_number_balanced(n) that checks if n is balanced.
"""


def is_number_balanced(n):
    n_string = str(n)
    digits_count = len(n_string)
    
    if digits_count == 1:
        return True

    left_sum = 0
    right_sum = 0

    for i in range(digits_count // 2):
        left_sum += int(n_string[i])
        right_sum += int(n_string[digits_count - i - 1])

    return left_sum == right_sum


def main():
    n = int(input("Enter a number to get if it's balanced: "))
    print(is_number_balanced(n))


if __name__ == '__main__':
    main()
