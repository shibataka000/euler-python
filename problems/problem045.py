# coding: utf-8

import itertools


def triangular():
    return map(lambda n: n * (n + 1) / 2, itertools.count(1))


def pentagonal():
    return map(lambda n: n * (3 * n - 1) / 2, itertools.count(1))


def hexagonal():
    return map(lambda n: n * (2 * n - 1), itertools.count(1))


def solve():
    t_gen, p_gen, h_gen = triangular(), pentagonal(), hexagonal()
    t, p = next(t_gen), next(p_gen)
    for h in h_gen:
        while t < h:
            t = next(t_gen)
        while p < h:
            p = next(p_gen)
        if t == p == h > 40755:
            return h
