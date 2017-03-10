# coding: utf-8

import itertools

import math_ext
import itertools_ext


def solve():
    seq = range(9, 0, -1)
    seq = map(math_ext.pandigital, seq)
    seq = map(sorted, seq)
    seq = map(reversed, seq)
    seq = itertools.chain.from_iterable(seq)
    return itertools_ext.find(math_ext.is_prime, seq)
