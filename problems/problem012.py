# coding: utf-8

import itertools
import itertools_ext


def triangular_number():
    for i in itertools.count(1):
        yield sum(range(i + 1))


def get_divisors(x):
    if x == 1:
        return [1]

    divisors = [1]
    for i in itertools.count(2):
        if x % i == 0:
            if i * i == x:
                divisors = divisors + [i] + [x / j for j in reversed(divisors)]
                return divisors
            elif divisors[-1] * i == x:
                divisors = divisors + [x / j for j in reversed(divisors)]
                return divisors
            else:
                divisors.append(i)


def solve():
    return itertools_ext.find(
        lambda x: len(get_divisors(x)) >= 500,
        triangular_number()
    )
