# coding: utf-8

import itertools

import pytest

import math_ext


def test_primes():
    primes_list = itertools.takewhile(lambda x: x <= 100, math_ext.primes())
    primes_list = list(primes_list)
    assert primes_list == [2, 3, 5, 7, 11, 13, 17, 19,
                           23, 29, 31, 37, 41, 43, 47,
                           53, 59, 61, 67, 71, 73, 79,
                           83, 89, 97]


def test_product():
    assert math_ext.product([1, 2, 3]) == 6
    with pytest.raises(Exception):
        math_ext.product([])


def test_get_divisors():
    assert math_ext.get_divisors(1) == [1]
    assert math_ext.get_divisors(3) == [1, 3]
    assert math_ext.get_divisors(6) == [1, 2, 3, 6]
    assert math_ext.get_divisors(9) == [1, 3, 9]
    assert math_ext.get_divisors(10) == [1, 2, 5, 10]
    assert math_ext.get_divisors(15) == [1, 3, 5, 15]
    assert math_ext.get_divisors(21) == [1, 3, 7, 21]
    assert math_ext.get_divisors(28) == [1, 2, 4, 7, 14, 28]
