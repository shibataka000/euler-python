# coding: utf-8

import itertools

from math_euler import fibonacci


def solve():
    fib_list = itertools.takewhile(lambda x: x < 4000000, fibonacci())
    even_fib_list = filter(lambda x: x % 2 == 0, fib_list)
    ans = sum(even_fib_list)
    return ans
