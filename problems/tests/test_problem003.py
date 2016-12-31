# coding: utf-8

import problems.problem003 as problem


def test_prime_decompose():
    assert problem.prime_decompose(1) == [1]
    assert problem.prime_decompose(2) == [2]
    assert problem.prime_decompose(4) == [2, 2]
    assert problem.prime_decompose(6) == [2, 3]
    assert problem.prime_decompose(8) == [2, 2, 2]
    assert problem.prime_decompose(9) == [3, 3]
    assert problem.prime_decompose(10) == [2, 5]
    assert problem.prime_decompose(12) == [2, 2, 3]
    assert problem.prime_decompose(13195) == [5, 7, 13, 29]


def test_solve():
    assert problem.solve() == 6857
