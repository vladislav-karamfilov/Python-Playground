"""
Given an integer, implement a function, called prime_numbers(n).
Use Sieve of Eratosthenes to find all the prime numbers less than or equal to n.
"""


from math import sqrt


def prime_numbers(n):
    if n < 0:
        raise ValueError('No negative prime numbers!')
    
    primes_sieve = [True for _ in range(2, n + 1)]
    for i in range(2, int(sqrt(n)) + 1):
        if primes_sieve[i - 2]:
            for j in range(i * i, n + 1, i):
                primes_sieve[j - 2] = False

    i = 2
    result = []
    for is_prime in primes_sieve:
        if is_prime:
            result.append(i)
        i += 1
    
    return result


def main():
    n = int(input('Enter a number to get all prime numbers less than or equal to it: '))
    print(prime_numbers(n))


if __name__ == '__main__':
    main()
