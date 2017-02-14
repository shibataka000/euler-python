# coding: utf-8

import itertools

import math_ext


def is_truncatable_prime(p):
    if p < 10:
        return False
    p_str = str(p)
    for i in range(1, len(p_str)):
        left = int(p_str[:i])
        right = int(p_str[i:])
        if not math_ext.is_prime(left) or not math_ext.is_prime(right):
            return False
    return True


def get_truncable_primes():
    return filter(is_truncatable_prime, math_ext.primes())


def solve():
    return sum(itertools.islice(get_truncable_primes(), 11))
