# coding: utf-8

import problems.problem053 as problem


def test_get_number_of_combinations():
    problem.get_number_of_combinations(5, 3) == 10


def test_solve():
    assert problem.solve() == 4075
