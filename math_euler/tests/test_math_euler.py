# coding: utf-8

import itertools

import math_euler


def test_fibonacci():
    fib = math_euler.fibonacci()
    assert next(fib) == 1
    assert next(fib) == 2
    assert next(fib) == 3
    assert next(fib) == 5
    assert next(fib) == 8
    assert next(fib) == 13
    assert next(fib) == 21
    assert next(fib) == 34
    assert next(fib) == 55


def test_primes():
    primes_list = itertools.takewhile(lambda x: x <= 100, math_euler.primes())
    primes_list = list(primes_list)
    assert primes_list == [2, 3, 5, 7, 11, 13, 17, 19,
                           23, 29, 31, 37, 41, 43, 47,
                           53, 59, 61, 67, 71, 73, 79,
                           83, 89, 97]


def test_prime_decompose():
    assert math_euler.prime_decompose(1) == [1]
    assert math_euler.prime_decompose(2) == [2]
    assert math_euler.prime_decompose(4) == [2, 2]
    assert math_euler.prime_decompose(6) == [2, 3]
    assert math_euler.prime_decompose(8) == [2, 2, 2]
    assert math_euler.prime_decompose(9) == [3, 3]
    assert math_euler.prime_decompose(10) == [2, 5]
    assert math_euler.prime_decompose(12) == [2, 2, 3]
    assert math_euler.prime_decompose(13195) == [5, 7, 13, 29]


def test_gcd():
    assert math_euler.gcd(2, 1) == 1
    assert math_euler.gcd(2, 2) == 2
    assert math_euler.gcd(2, 3) == 1
    assert math_euler.gcd(2, 4) == 2


def test_lcm():
    assert math_euler.lcm(2, 3) == 6
    assert math_euler.lcm(2, 4) == 4
