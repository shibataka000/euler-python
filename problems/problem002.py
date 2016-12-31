# coding: utf-8

import itertools


def fibonacci():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b


def solve():
    fib_list = itertools.takewhile(lambda x: x < 4000000, fibonacci())
    even_fib_list = filter(lambda x: x % 2 == 0, fib_list)
    ans = sum(even_fib_list)
    return ans
