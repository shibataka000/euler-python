# coding: utf-8

import problems.problem028 as problem


def corners():
    corn = problem.corners()
    assert next(corn) == 1
    assert next(corn) == 3
    assert next(corn) == 5
    assert next(corn) == 7
    assert next(corn) == 9
    assert next(corn) == 13
    assert next(corn) == 17
    assert next(corn) == 21
    assert next(corn) == 25
    assert next(corn) == 31
    assert next(corn) == 37
    assert next(corn) == 43
    assert next(corn) == 49


def test_solve():
    assert problem.solve() == 669171001
