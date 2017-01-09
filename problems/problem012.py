# coding: utf-8

import itertools

import itertools_ext
import math_ext


def triangular_number():
    for i in itertools.count(1):
        yield sum(range(i + 1))


def solve():
    return itertools_ext.find(
        lambda x: len(math_ext.get_divisors(x)) >= 500,
        triangular_number()
    )
