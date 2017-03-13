# coding: utf-8

import itertools_ext
import math_ext


def solve():
    return itertools_ext.find(
        lambda x: len(math_ext.get_divisors(x)) >= 500,
        math_ext.triangular()
    )
