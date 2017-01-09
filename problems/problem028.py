# coding: utf-8

import itertools


def corners():
    n = 1
    yield n
    step = 2
    while True:
        for i in range(4):
            n += step
            yield n
        step += 2


def solve():
    L = itertools.islice(corners(), 1000 * 2 + 1)
    return sum(L)
