# coding: utf-8

import itertools

import math_ext


def solve():
    seq = itertools.combinations(range(100, 1000), 2)
    seq = map(lambda x: x[0] * x[1], seq)
    seq = filter(math_ext.is_palindromic_number, seq)
    return max(seq)
