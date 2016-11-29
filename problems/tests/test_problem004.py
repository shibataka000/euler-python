# coding: utf-8

import problems.problem004 as problem


def test_is_palindromic_number():
    assert problem.is_palindromic_number(1) is True
    assert problem.is_palindromic_number(9009) is True
    assert problem.is_palindromic_number(9008) is False


def test_solve():
    assert problem.solve() == 906609
