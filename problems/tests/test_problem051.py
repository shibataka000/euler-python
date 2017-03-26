# coding: utf-8

import math_ext

import problems.problem051 as problem


def test_get_replaced_numbers():
    expect = [13, 23, 33, 43, 53, 63, 73, 83, 93]
    assert problem.get_replaced_numbers(13, 1) == expect


def test_get_all_replaced_numbers():
    expect = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
              23, 33, 43, 53, 63, 73, 83, 93]
    assert problem.get_all_replaced_numbers(13) == expect


def test_has_number_of_primes():
    assert problem.has_number_of_primes(range(0, 11), 3)
    assert problem.has_number_of_primes(range(0, 11), 4)
    assert not problem.has_number_of_primes(range(0, 11), 5)


def test_has_number_of_replaced_primes():
    assert problem.has_number_of_replaced_primes(121313, 8)

    primes = math_ext.primes()
    p = next(primes)
    while p < 56003:
        assert not problem.has_number_of_replaced_primes(p, 7)
        p = next(primes)
    assert problem.has_number_of_replaced_primes(56003, 7)


def test_solve():
    assert problem.solve() == 121313
