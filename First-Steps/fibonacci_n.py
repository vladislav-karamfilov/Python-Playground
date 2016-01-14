"""
- Implement a function, called fibonacci(n) that returns a list with the first n members of the Fibonacci sequence.

- Implement a function, called fib_number(n), which takes an integer n and returns a number, which is formed by
concatenating the first n Fibonacci numbers. For example, if n = 3, the result is 112.
"""


def fibonacci(n):
    if n < 1:
        raise ValueError('Negative or zero position from Fibonacci sequence does not exist!')

    if n == 1:
        members = [1]
    else:
        members = [1, 1]
        for i in range(2, n):
            new_member = members[i - 1] + members[i - 2]
            members.append(new_member)

    return members


def fib_number(n):
    fibonacci_members = fibonacci(n)
    return int(''.join([str(x) for x in fibonacci_members]))


def main():
    n = int(input(
        'Enter N to get the first N members of the Fibonacci sequence and the number formed by concatenating them: '))
    fibonacci_members = fibonacci(n)
    print('First {0} members of the Fibonacci sequence are: {1}'.format(n, fibonacci_members))
    print('The number formed by concatenating the first {0} members of the Fibonacci sequence is: {1}'
          .format(n, fib_number(n)))


if __name__ == '__main__':
    main()
