# coding: utf-8

import math_ext


def decompose_pandigital_product(x):
    x = str(x)
    c = int("".join(x[5:9]))
    for i in range(1, 5):
        a = int("".join(x[:i]))
        b = int("".join(x[i:5]))
        if a * b == c:
            return (a, b, c)


def solve():
    L = [decompose_pandigital_product(x)
         for x in math_ext.pandigital(9)]
    return sum(set([x[2] for x in L if x is not None]))
