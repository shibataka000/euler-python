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


def test_get_divisors():
    assert problem.get_divisors(1) == [1]
    assert problem.get_divisors(3) == [1, 3]
    assert problem.get_divisors(6) == [1, 2, 3, 6]
    assert problem.get_divisors(9) == [1, 3, 9]
    assert problem.get_divisors(10) == [1, 2, 5, 10]
    assert problem.get_divisors(15) == [1, 3, 5, 15]
    assert problem.get_divisors(21) == [1, 3, 7, 21]
    assert problem.get_divisors(28) == [1, 2, 4, 7, 14, 28]


def test_solve():
    assert problem.solve() == 76576500
