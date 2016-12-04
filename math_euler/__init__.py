# coding: utf-8


def fibonacci():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b


def primes():
    yield 2
    primes_list = [2]
    n = 3
    while True:
        if all([n % p != 0 for p in primes_list]):
            yield n
            primes_list.append(n)
        n += 2


def prime_decompose(x):
    if x == 1:
        return [1]
    factors = []
    for p in primes():
        if p > x:
            break
        while x % p == 0:
            factors.append(p)
            x /= p
    return factors
