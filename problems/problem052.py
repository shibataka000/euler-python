# coding: utf-8

import itertools
from functools import reduce

import itertools_ext


def is_permuted_multiples(n):
    L = [sorted(str(n * i)) for i in range(1, 7)]
    r = reduce(lambda a, b: a if a == b else None, L)
    return r is not None


def solve():
    seq = itertools.count(1)
    return itertools_ext.find(is_permuted_multiples, seq)
