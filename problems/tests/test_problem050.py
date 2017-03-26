# coding: utf-8

import problems.problem050 as problem


def test_slice_seq():
    assert list(problem.slice_seq(range(10), 3, 7)) == [3, 4, 5, 6]


def test_get_max_consecutive_prime_sum():
    assert problem.get_max_consecutive_prime_sum(100) == 41
    assert problem.get_max_consecutive_prime_sum(1000) == 953


def test_solve():
    assert problem.solve() == 997651
