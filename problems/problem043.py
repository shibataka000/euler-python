# coding: utf-8

import math_ext


def is_sub_string_divisable(n):
    if n < 10 ** 9:
        return False
    str_n = str(n)
    if not int(str_n[3]) % 2 == 0:
        return False
    if not int(str_n[5]) % 5 == 0:
        return False
    p = [2, 3, 5, 7, 11, 13, 17]
    L = [int(str_n[i + 1:i + 4]) for i in range(7)]
    return all([n_sub % p[i] == 0 for i, n_sub in enumerate(L)])


def solve():
    return sum([p for p in math_ext.pandigital(range(10))
                if is_sub_string_divisable(p)])
