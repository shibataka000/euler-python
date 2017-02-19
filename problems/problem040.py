# coding: utf-8

import itertools

import math_ext


def champernownes_constant():
    for i in itertools.count(start=1):
        for j in str(i):
            yield int(j)


def nth(iterable, n):
    L = itertools.islice(iterable, n, n + 1)
    L = list(L)
    assert len(L) == 1
    return L[0]


def solve():
    return math_ext.product(
        [nth(champernownes_constant(), 10 ** i - 1) for i in range(7)]
    )
         
