# coding: utf-8

import problems.problem027 as problem


def is_prime():
    assert not problem.is_prime(-1)
    assert not problem.is_prime(0)
    assert not problem.is_prime(1)
    assert problem.is_prime(2)
    assert problem.is_prime(3)
    assert not problem.is_prime(4)
    assert problem.is_prime(5)
    assert not problem.is_prime(6)
    assert problem.is_prime(7)
    assert not problem.is_prime(8)
    assert not problem.is_prime(9)
    assert not problem.is_prime(10)


def test_generate_primes():
    pass


def test_get_prime_length():
    assert problem.get_prime_length(1, 41) == 40
    assert problem.get_prime_length(-79, 1601) == 80


def test_solve():
    assert problem.solve() == -59231
