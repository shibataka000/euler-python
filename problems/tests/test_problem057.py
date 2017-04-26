# coding: utf-8

from fractions import Fraction

import problems.problem057 as problem


def test_reciprocal():
    f = Fraction(2, 4)
    assert problem.reciprocal(f) == Fraction(2, 1)


def test_square_root_as_continued_fractions():
    gen = problem.square_root_as_continued_fractions()
    assert next(gen) == Fraction(3, 2)
    assert next(gen) == Fraction(7, 5)
    assert next(gen) == Fraction(17, 12)
    assert next(gen) == Fraction(41, 29)
    assert next(gen) == Fraction(99, 70)
    assert next(gen) == Fraction(239, 169)
    assert next(gen) == Fraction(577, 408)


def test_digits():
    assert problem.digits(1) == 1
    assert problem.digits(10) == 2


def test_solve():
    assert problem.solve() == 153
