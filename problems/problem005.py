# coding: utf-8

from functools import reduce
from fractions import gcd


def lcm(a, b):
    return int(a * b / gcd(a, b))


def solve():
    return reduce(lambda x, y: lcm(x, y), list(range(1, 21)))
