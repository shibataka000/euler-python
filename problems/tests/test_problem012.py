# coding: utf-8

import problems.problem012 as problem


def test_triangular_number():
    triangular_number = problem.triangular_number()
    assert next(triangular_number) == 1
    assert next(triangular_number) == 3
    assert next(triangular_number) == 6
    assert next(triangular_number) == 10
    assert next(triangular_number) == 15
    assert next(triangular_number) == 21
    assert next(triangular_number) == 28


def test_solve():
    assert problem.solve() == 76576500
