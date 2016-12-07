# coding: utf-8

from functools import reduce

from math_euler import lcm


def solve():
    return reduce(lambda x, y: lcm(x, y), list(range(1, 21)))
