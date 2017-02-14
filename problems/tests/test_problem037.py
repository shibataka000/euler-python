# coding: utf-8

import itertools

import problems.problem037 as problem


def test_is_truncatable_prime():
    assert not problem.is_truncatable_prime(2)
    assert not problem.is_truncatable_prime(3)
    assert not problem.is_truncatable_prime(5)
    assert not problem.is_truncatable_prime(7)
    assert problem.is_truncatable_prime(3797)


def test_get_truncable_primes():
    expect = [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
    actual = list(itertools.islice(problem.get_truncable_primes(), 11))
    assert expect == actual


def test_solve():
    assert problem.solve() == 748317
