# coding: utf-8

import math_ext


def prime_decompose(x):
    if x == 1:
        return [1]
    factors = []
    for p in math_ext.primes():
        if p > x:
            break
        while x % p == 0:
            factors.append(p)
            x /= p
    return factors


def solve():
    factors = prime_decompose(600851475143)
    return max(factors)
