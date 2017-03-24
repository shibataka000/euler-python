# coding: utf-8

import functools
import itertools

import math_ext


primes_cache = [2, 3]
sieve_cache = [True]


def primes():
    def mark_sieve(prime, sieve):
        i, l = 2 * prime, len(sieve)
        while i < l:
            sieve[i] = False
            i += prime

    primes = primes_cache
    sieve = sieve_cache
    for p in primes:
        yield p
    for i in itertools.count(max(primes) + 2, 2):
        if i >= len(sieve):
            sieve += [True] * (9 * len(sieve))
            for p in primes:
                mark_sieve(p, sieve)
        if sieve[i]:
            primes.append(i)
            mark_sieve(i, sieve)
            yield i


def prime_decompose(x):
    if x == 1 or math_ext.is_prime(x):
        return [x]
    factors = []
    for p in primes():
        if p > x:
            break
        if x % p == 0:
            q = 1
            while x % p == 0:
                x = int(x / p)
                q *= p
            factors.append(q)
            if math_ext.is_prime(x):
                factors.append(x)
                break
    return sorted(factors)


def solve():
    i, n = 1, 4
    while True:
        decomposed = [set(prime_decompose(i + j)) for j in range(n)]
        print(i, decomposed)
        if all([len(d) == n for d in decomposed]):
            unioned = functools.reduce(lambda a, b: a | b, decomposed)
            if len(unioned) == n ** 2:
                return i
            else:
                step = 1
        else:
            k = max([j for j, d in enumerate(decomposed) if len(d) != n])
            step = k + 1
        i += step
