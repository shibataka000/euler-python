# coding: utf-8

import itertools

import problems.problem040 as problem


def test_champernownes_constant():
    expect = [1, 2, 3, 4, 5, 6, 7, 8, 9,
              1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 2, 0]
    actual = itertools.islice(problem.champernownes_constant(), 0, len(expect))
    assert list(actual) == expect


def test_nth():
    assert problem.nth(itertools.count(), 0) == 0
    assert problem.nth(itertools.count(), 1) == 1
    assert problem.nth(itertools.count(), 2) == 2
    assert problem.nth(problem.champernownes_constant(), 12) == 1


def test_solve():
    assert problem.solve() == 210
