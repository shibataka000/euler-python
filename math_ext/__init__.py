# coding: utf-8

import itertools
import functools
import random


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


def is_prime(p, k=0):
    primes = [2, 3, 5, 7]
    if p <= 1:
        return False
    elif p in primes:
        return True
    elif any([p % i == 0 for i in primes]):
        return False
    elif pow(2, p - 1, p) != 1:
        return False
    elif k >= 1:
        n, s = p, 1
        while (n - 1) % (2 ** s) != 0:
            s += 1
        d = (n - 1) // (2 ** s)
        for i in range(k):
            a = random.randint(1, n - 1)
            b1 = pow(a, d, n) != 1
            b2 = all([pow(a, (2 ** r) * d, n) != n - 1 for r in range(s)])
            if b1 and b2:
                return False
        return True
    else:
        return True


def pandigital(L):
    seed = "".join([str(i) for i in L])
    for x in itertools.permutations(seed):
        yield int("".join(x))


def odd(x):
    return x % 2 == 1


def even(x):
    return x % 2 == 0


def pentagonal():
    for n in itertools.count(1):
        yield int(n * (3 * n - 1) / 2)


def triangular():
    for n in itertools.count(1):
        yield int(n * (n + 1) / 2)


def is_palindromic_number(x):
    a = str(x)
    b = str(x)[::-1]
    return a == b


def corners():
    n = 1
    yield n
    step = 2
    while True:
        for i in range(4):
            n += step
            yield n
        step += 2
