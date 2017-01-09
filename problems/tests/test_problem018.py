# coding: utf-8

import problems.problem018 as problem


def test_get_max_route_value():
    triangle = """3
7 4
2 4 6
8 5 9 3"""
    problem.get_max_route_value(triangle) == 23


def test_solve():
    assert problem.solve() == 1074
