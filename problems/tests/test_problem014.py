# coding: utf-8

import problems.problem014 as problem


def test_collatz():
    assert list(problem.collatz(13)) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_get_collatz_len():
    assert problem.get_collatz_len(1, {}) == 1
    assert problem.get_collatz_len(13, {}) == 10
    assert problem.get_collatz_len(13, {40: 0}) == 1


def test_solve():
    assert problem.solve() == 837799
