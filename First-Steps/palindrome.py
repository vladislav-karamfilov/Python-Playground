"""
Implement a function, called palindrome(obj), which takes an object (could be anything) and checks if it's string
representation is a palindrome.

For example, the integer 121 and the string "kapak" are palindromes. The function should work with both.
"""


def palindrome(obj):
    string = str(obj)
    reversed_string = string[::-1]
    return string == reversed_string


def main():
    obj = 28782
    print('{0} is palindrome: {1}'.format(obj, palindrome(obj)))
    obj = [1, 2, 4, 5]
    print('{0} is palindrome: {1}'.format(obj, palindrome(obj)))
    obj = (1, 2, 4, 2, 1)
    print('{0} is palindrome: {1}'.format(obj, palindrome(obj)))
    obj = 'ABBA'
    print('{0} is palindrome: {1}'.format(obj, palindrome(obj)))


if __name__ == '__main__':
    main()
