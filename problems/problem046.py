# coding: utf-8

import itertools

import math_ext
import itertools_ext


def is_goldbach(n):
    for i in range(1, n + 1):
        j = n - 2 * (i ** 2)
        print("{} = {} + 2 * {} ^ 2".format(n, j, i))
        if j < 0:
            return False
        if j == 1 or math_ext.is_prime(j):
            return True
    return False


def composite_numbers():
    return filter(lambda n: not math_ext.is_prime(n), itertools.count(4))


def odd_composite_numbers():
    return filter(math_ext.odd, composite_numbers())
    

def solve():
    return itertools_ext.find(
        lambda n: not is_goldbach(n),
        odd_composite_numbers()
    )
