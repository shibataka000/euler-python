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


def test_get_true_divisors():
    assert math_ext.get_true_divisors(1) == []
    assert math_ext.get_true_divisors(3) == [1]
    assert math_ext.get_true_divisors(6) == [1, 2, 3]
    assert math_ext.get_true_divisors(9) == [1, 3]
    assert math_ext.get_true_divisors(10) == [1, 2, 5]
    assert math_ext.get_true_divisors(15) == [1, 3, 5]
    assert math_ext.get_true_divisors(21) == [1, 3, 7]
    assert math_ext.get_true_divisors(28) == [1, 2, 4, 7, 14]


def test_fibonacci():
    fib = math_ext.fibonacci()
    assert next(fib) == 1
    assert next(fib) == 1
    assert next(fib) == 2
    assert next(fib) == 3
    assert next(fib) == 5
    assert next(fib) == 8
    assert next(fib) == 13
    assert next(fib) == 21
    assert next(fib) == 34
    assert next(fib) == 55


def test_is_prime():
    assert not math_ext.is_prime(-1)
    assert not math_ext.is_prime(0)
    assert not math_ext.is_prime(1)
    assert math_ext.is_prime(2)
    assert math_ext.is_prime(3)
    assert not math_ext.is_prime(4)
    assert math_ext.is_prime(5)
    assert not math_ext.is_prime(6)
    assert math_ext.is_prime(7)
    assert not math_ext.is_prime(8)
    assert not math_ext.is_prime(9)
    assert not math_ext.is_prime(10)


def test_pandigital():
    expect = [1234, 1243, 1324, 1342, 1423, 1432,
              2134, 2143, 2314, 2341, 2413, 2431,
              3124, 3142, 3214, 3241, 3412, 3421,
              4123, 4132, 4213, 4231, 4312, 4321]
    actual = list(math_ext.pandigital(range(1, 5)))
    assert expect == actual


def test_odd():
    assert math_ext.odd(-1)
    assert not math_ext.odd(0)
    assert math_ext.odd(1)


def test_even():
    assert not math_ext.even(-1)
    assert math_ext.even(0)
    assert not math_ext.even(1)


def test_pentagonal():
    seq = math_ext.pentagonal()
    expect = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
    actual = [next(seq) for i in range(len(expect))]
    assert expect == actual


def test_triangular():
    seq = math_ext.triangular()
    expect = [1, 3, 6, 10, 15]
    actual = [next(seq) for i in range(len(expect))]
    assert expect == actual


def test_is_palindromic_number():
    assert math_ext.is_palindromic_number(1) is True
    assert math_ext.is_palindromic_number(9009) is True
    assert math_ext.is_palindromic_number(9008) is False


def test_corners():
    corn = math_ext.corners()
    assert next(corn) == 1
    assert next(corn) == 3
    assert next(corn) == 5
    assert next(corn) == 7
    assert next(corn) == 9
    assert next(corn) == 13
    assert next(corn) == 17
    assert next(corn) == 21
    assert next(corn) == 25
    assert next(corn) == 31
    assert next(corn) == 37
    assert next(corn) == 43
    assert next(corn) == 49
