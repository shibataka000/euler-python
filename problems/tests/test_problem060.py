# coding: utf-8

import itertools

import problems.problem060 as problem


def test_is_prime_pair():
    for (p1, p2) in itertools.permutations([3, 7, 109, 673], 2):
        problem.is_prime_pair(p1, p2)


def test_solve():
    assert problem.solve() == 26033
