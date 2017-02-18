# coding: utf-8

import problems.problem039 as problem


def test_get_right_triangle_edges():
    expect = [(50, 40, 30), (51, 45, 24), (52, 48, 20)]
    actual = problem.get_right_triangle_edges(120)
    assert expect == actual


def test_solve():
    assert problem.solve() == 840
