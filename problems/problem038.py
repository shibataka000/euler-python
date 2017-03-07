# coding: utf-8

import math_ext


def solve():
    for n in range(9876, 0, -1):
        L = list(str(n) + str(n * 2))
        i = 3
        while len(L) < 9:
            L += str(n * i)
            i += 1
        m = int("".join(L))
        if math_ext.is_pandigital(m):
            return m
