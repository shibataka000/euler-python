# coding: utf-8

import itertools
import functools


def primes():
    def mark_sieve(prime, sieve):
        i, l = 2 * prime, len(sieve)
        while i < l:
            sieve[i] = False
            i += prime

    yield 2
    primes = [2]
    sieve = [True]
    for i in itertools.count(3, 2):
        if i >= len(sieve):
            sieve = [True] * (10 * len(sieve))
            for p in primes:
                mark_sieve(p, sieve)
        if sieve[i]:
            primes.append(i)
            mark_sieve(i, sieve)
            yield i


def product(L):
    return functools.reduce(lambda a, b: a * b, L)


def get_divisors(x):
    if x == 1:
        return [1]

    divisors = [1]
    for i in itertools.count(2):
        if x % i == 0:
            if i * i == x:
                rest = [round(x / j) for j in reversed(divisors)]
                return divisors + [i] + rest
            elif divisors[-1] * i == x:
                rest = [round(x / j) for j in reversed(divisors)]
                return divisors + rest
            else:
                divisors.append(i)


def get_true_divisors(x):
    return get_divisors(x)[:-1]


def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(p):
    primes = [2, 3, 5, 7]
    if p <= 1:
        return False
    elif p in primes:
        return True
    elif any([p % i == 0 for i in primes]):
        return False
    else:
        return (2 ** (p - 1)) % p == 1


def pandigital(L):
    seed = "".join([str(i) for i in L])
    for x in itertools.permutations(seed):
        yield int("".join(x))


def odd(x):
    return x % 2 == 1


def even(x):
    return x % 2 == 0
