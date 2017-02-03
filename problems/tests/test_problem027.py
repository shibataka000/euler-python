# coding: utf-8

import problems.problem027 as problem


def test_generate_primes():
    pass


def test_get_prime_length():
    assert problem.get_prime_length(1, 41) == 40
    assert problem.get_prime_length(-79, 1601) == 80


def test_solve():
    assert problem.solve() == -59231
