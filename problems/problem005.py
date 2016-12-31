# coding: utf-8

from functools import reduce


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))


def solve():
    return reduce(lambda x, y: lcm(x, y), list(range(1, 21)))
