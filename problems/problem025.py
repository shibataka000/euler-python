# coding: utf-8

import math_ext
import itertools_ext


def solve():
    i, v = itertools_ext.find(
        lambda x: x[1] >= 10 ** (1000 - 1),
        enumerate(math_ext.fibonacci())
    )
    return i + 1
