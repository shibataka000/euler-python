# coding: utf-8

import problems.problem046 as problem


def test_is_goldbach():
    assert problem.is_goldbach(9)
    assert problem.is_goldbach(15)
    assert problem.is_goldbach(21)
    assert problem.is_goldbach(25)
    assert problem.is_goldbach(27)
    assert problem.is_goldbach(33)


def test_composite_numbers():
    seq = problem.composite_numbers()
    expect = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18,
              20, 21, 22, 24, 25, 26, 27, 28, 30]
    actual = [next(seq) for i in range(len(expect))]
    assert expect == actual


def test_odd_composite_numbers():
    seq = problem.odd_composite_numbers()
    expect = [9, 15, 21, 25, 27, 33]
    actual = [next(seq) for i in range(len(expect))]
    assert expect == actual


def test_solve():
    assert problem.solve() == 5777
