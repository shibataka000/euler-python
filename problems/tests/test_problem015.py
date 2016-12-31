# coding: utf-8

import problems.problem015 as problem


def test_factorial():
    assert problem.factorial(1) == 1
    assert problem.factorial(2) == 2
    assert problem.factorial(3) == 6
    assert problem.factorial(4) == 24


def test_solve():
    assert problem.solve() == 137846528820
