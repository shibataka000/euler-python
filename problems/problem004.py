# coding: utf-8

import itertools


def is_palindromic_number(x):
    a = str(x)
    b = str(x)[::-1]
    return a == b


def solve():
    seq = itertools.combinations(range(100, 1000), 2)
    seq = map(lambda x: x[0] * x[1], seq)
    seq = filter(is_palindromic_number, seq)
    return max(seq)
