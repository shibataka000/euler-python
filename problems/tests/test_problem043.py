# coding: utf-8

import problems.problem043 as problem


def test_is_sub_string_divisable():
    assert problem.is_sub_string_divisable(1406357289)


def test_solve():
    assert problem.solve() == 16695334890
