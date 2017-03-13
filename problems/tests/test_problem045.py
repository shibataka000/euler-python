# coding: utf-8

import problems.problem045 as problem


def test_triangular():
    seq = problem.triangular()
    expect = [1, 3, 6, 10, 15]
    actual = [next(seq) for i in range(len(expect))]
    assert expect == actual


def test_pentagonal():
    seq = problem.pentagonal()
    expect = [1, 5, 12, 22, 35]
    actual = [next(seq) for i in range(len(expect))]
    assert expect == actual


def test_hexagonal():
    seq = problem.hexagonal()
    expect = [1, 6, 15, 28, 45]
    actual = [next(seq) for i in range(len(expect))]
    assert expect == actual


def test_solve():
    assert problem.solve() == 1533776805
