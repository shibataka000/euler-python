# coding: utf-8

import problems.problem038 as problem


def test_is_pandigital_number():
    assert problem.is_pandigital_number(123456789)
    assert not problem.is_pandigital_number(111111111)
    assert not problem.is_pandigital_number(1234567890)
    assert problem.is_pandigital_number(932718654)


def test_solve():
    assert problem.solve() == 932718654
