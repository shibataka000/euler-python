# coding: utf-8

import problems.problem044 as problem


def test_pentagonal():
    seq = problem.pentagonal()
    expect = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
    actual = [next(seq) for i in range(len(expect))]
    assert expect == actual


def test_is_pentagonal_number():
    for n in range(1, 146):
        if n in [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]:
            assert problem.is_pentagonal_number(n)
        else:
            assert not problem.is_pentagonal_number(n)


def test_solve():
    assert problem.solve() == 5482660
