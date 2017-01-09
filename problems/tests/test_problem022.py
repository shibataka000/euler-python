# coding: utf-8

import problems.problem022 as problem


def test_get_score():
    assert problem.get_score("COLIN") == 53


def test_solve():
    assert problem.solve() == 871198282
