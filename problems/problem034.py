# coding: utf-8

import math


def sum_factorial(n):
    return sum([math.factorial(int(x)) for x in str(n)])


def solve():
    return sum([i for i in range(3, 10 ** 7)
                if sum_factorial(i) == i])
