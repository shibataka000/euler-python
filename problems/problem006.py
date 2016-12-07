# coding: utf-8


def solve():
    a = sum([n ** 2 for n in range(1, 101)])
    b = sum([n for n in range(1, 101)]) ** 2
    return abs(a - b)
