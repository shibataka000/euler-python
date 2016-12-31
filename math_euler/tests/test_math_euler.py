# coding: utf-8

import itertools

import math_euler


def test_primes():
    primes_list = itertools.takewhile(lambda x: x <= 100, math_euler.primes())
    primes_list = list(primes_list)
    assert primes_list == [2, 3, 5, 7, 11, 13, 17, 19,
                           23, 29, 31, 37, 41, 43, 47,
                           53, 59, 61, 67, 71, 73, 79,
                           83, 89, 97]
