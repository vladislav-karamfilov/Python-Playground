"""
Implement a function get_largest_palindrome(n), which return the largest palindrome smaller than n.
Given number n can also be palindrome.
"""

from palindrome import palindrome


def get_largest_palindrome(n):
    if n < 0:
        raise ValueError('Negative numbers cannot be palindromes!')

    while n > 0:
        n -= 1
        if palindrome(n):
            return n
        
    return 0


def main():
    n = int(input('Enter a number to get the largest palindrome smaller than it: '))
    print(get_largest_palindrome(n))


if __name__ == '__main__':
    main()
