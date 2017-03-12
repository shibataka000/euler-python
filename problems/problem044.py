# coding: utf-8

import math

import itertools


def nth_pentagonal_number(n):
    return int(n * (3 * n - 1) / 2)


def is_pentagonal_number(n):
    i = (1 + math.sqrt(1 + 24 * n)) / 6
    return i.is_integer()


def solve():
    ans = None
    for i in itertools.count(1):
        a = nth_pentagonal_number(i)
        b = nth_pentagonal_number(i - 1)
        if ans and a - b > ans:
            return ans
        for j in range(i - 2, 0, -1):
            b = nth_pentagonal_number(j)
            if ans and a - b > ans:
                break
            if is_pentagonal_number(a - b) and is_pentagonal_number(a + b):
                ans = a - b
                break
