# coding: utf-8

import math_ext


def solve():
    for d in range(9, 0, -1):
        for p in reversed(sorted(math_ext.pandigital(d))):
            if math_ext.is_prime(p):
                return p
