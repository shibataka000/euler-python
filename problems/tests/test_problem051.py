# coding: utf-8

import problems.problem051 as problem


def test_get_replaced_primes():
    assert problem.get_replaced_primes(13) == [13, 23, 43, 53, 73, 83]
    assert problem.get_replaced_primes(56003) == [
        56003, 56113, 56333, 56443, 56663, 56773, 56993]


def test_solve():
    assert problem.solve() == 121313
