# coding: utf-8

import math


def solve():
    n = 20
    return int(math.factorial(n * 2) / (math.factorial(n) * math.factorial(n)))
