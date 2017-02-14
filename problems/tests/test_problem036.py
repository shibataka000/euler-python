# coding: utf-8

import problems.problem036 as problem


def test_binary():
    assert problem.binary(0) == 0
    assert problem.binary(1) == 1
    assert problem.binary(2) == 10


def test_reverse():
    assert problem.reverse(123) == 321


def test_solve():
    assert problem.solve() == 872187
