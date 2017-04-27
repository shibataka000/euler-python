# coding: utf-8

import itertools

import math_ext


def solve():
    L = itertools.islice(math_ext.corners(), 1000 * 2 + 1)
    return sum(L)
