# coding: utf-8

import itertools

from math_ext import primes


def solve():
    return sum(itertools.takewhile(lambda x: x <= 2000000, primes()))
