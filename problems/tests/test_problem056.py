# coding: utf-8

import problems.problem056 as problem


def test_sum_of_each_digits():
    assert problem.sum_of_each_digits(100) == 1
    assert problem.sum_of_each_digits(123) == 6


def test_solve():
    assert problem.solve() == 972
