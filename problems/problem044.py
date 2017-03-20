# coding: utf-8

import math

import math_ext


def is_pentagonal_number(n):
    i = (1 + math.sqrt(1 + 24 * n)) / 6
    return i.is_integer()


def solve():
    for a in math_ext.pentagonal():
        for b in math_ext.pentagonal():
            if a - b <= 0:
                break
            if is_pentagonal_number(a - b) and is_pentagonal_number(a + b):
                return a - b
