# coding: utf-8

import problems.problem055 as problem


def test_is_lychrel_number():
    assert not problem.is_lychrel_number(47)
    assert not problem.is_lychrel_number(349)
    assert problem.is_lychrel_number(4994)
    assert problem.is_lychrel_number(196)
    assert problem.is_lychrel_number(10677)


def test_solve():
    assert problem.solve() == 249
