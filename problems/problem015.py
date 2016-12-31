# coding: utf-8

import math_euler


def factorial(n):
    return math_euler.product(range(1, n + 1))


def solve():
    n = 20
    return int(factorial(n * 2) / (factorial(n) * factorial(n)))
