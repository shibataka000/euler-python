# coding: utf-8

import math

import itertools


def is_pentagonal_number(n):
    i = (1 + math.sqrt(1 + 24 * n)) / 6
    return i.is_integer()


def pentagonal():
    for n in itertools.count(1):
        yield int(n * (3 * n - 1) / 2)


def solve():
    for a in pentagonal():
        for b in pentagonal():
            if a - b <= 0:
                break
            if is_pentagonal_number(a - b) and is_pentagonal_number(a + b):
                return a - b
