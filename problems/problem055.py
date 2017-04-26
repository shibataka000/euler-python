# coding: utf-8

import math_ext


def is_lychrel_number(n):
    for i in range(49):
        reversed_n = int(str(n)[::-1])
        n += reversed_n
        if math_ext.is_palindromic_number(n):
            return False
    return True


def solve():
    return len([i for i in range(1, 10000) if is_lychrel_number(i)])
