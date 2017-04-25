# coding: utf-8

import math


def get_number_of_combinations(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def solve():
    return len([(n, r)
                for n in range(1, 101)
                for r in range(1, n + 1)
                if get_number_of_combinations(n, r) >= 10 ** 6])
