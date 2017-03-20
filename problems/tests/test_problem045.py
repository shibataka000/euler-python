# coding: utf-8

import problems.problem045 as problem


def test_hexagonal():
    seq = problem.hexagonal()
    expect = [1, 6, 15, 28, 45]
    actual = [next(seq) for i in range(len(expect))]
    assert expect == actual


def test_solve():
    assert problem.solve() == 1533776805
