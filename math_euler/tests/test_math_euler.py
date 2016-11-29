# coding: utf-8

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
