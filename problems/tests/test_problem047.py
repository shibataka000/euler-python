# coding: utf-8

import itertools

import problems.problem047 as problem


def test_primes():
    primes_list = itertools.takewhile(lambda x: x <= 100, problem.primes())
    primes_list = list(primes_list)
    assert primes_list == [2, 3, 5, 7, 11, 13, 17, 19,
                           23, 29, 31, 37, 41, 43, 47,
                           53, 59, 61, 67, 71, 73, 79,
                           83, 89, 97]


def test_prime_decompose():
    assert problem.prime_decompose(1) == [1]
    assert problem.prime_decompose(2) == [2]
    assert problem.prime_decompose(4) == [4]
    assert problem.prime_decompose(6) == [2, 3]
    assert problem.prime_decompose(8) == [8]
    assert problem.prime_decompose(9) == [9]
    assert problem.prime_decompose(10) == [2, 5]
    assert problem.prime_decompose(12) == [3, 4]
    assert problem.prime_decompose(13195) == [5, 7, 13, 29]


def test_solve():
    assert problem.solve() == 134043
