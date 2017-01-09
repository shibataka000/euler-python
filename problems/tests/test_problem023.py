# coding: utf-8

import problems.problem023 as problem


def test_abundant_number():
    abu = problem.abundant_number()
    assert next(abu) == 12
    assert next(abu) == 18
    assert next(abu) == 20
    assert next(abu) == 24
    assert next(abu) == 30
    assert next(abu) == 36
    assert next(abu) == 40
    assert next(abu) == 42
    assert next(abu) == 48


def test_solve():
    assert problem.solve() == 4179871
