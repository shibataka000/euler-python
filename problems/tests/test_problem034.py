# coding: utf-8

import problems.problem034 as problem


def test_sum_factorial():
    assert problem.sum_factorial(145) == 145


def test_solve():
    assert problem.solve() == 40730
