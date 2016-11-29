# coding: utf-8

from math_euler import prime_decompose


def solve():
    factors = prime_decompose(600851475143)
    return max(factors)
