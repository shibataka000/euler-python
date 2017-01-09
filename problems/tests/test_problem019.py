# coding: utf-8

import problems.problem019 as problem


def test_is_uruu():
    assert not problem.is_uruu(1900)
    assert not problem.is_uruu(1901)
    assert problem.is_uruu(1904)


def test_get_days():
    assert problem.get_days(1901, 1) == 31
    assert problem.get_days(1901, 2) == 28
    assert problem.get_days(1904, 2) == 29
    assert problem.get_days(1901, 4) == 30
    

def test_solve():
    assert problem.solve() == 171
