# coding: utf-8

import problems.problem002 as problem


def test_fibonacci():
    fib = problem.fibonacci()
    assert next(fib) == 1
    assert next(fib) == 2
    assert next(fib) == 3
    assert next(fib) == 5
    assert next(fib) == 8
    assert next(fib) == 13
    assert next(fib) == 21
    assert next(fib) == 34
    assert next(fib) == 55


def test_solve():
    assert problem.solve() == 4613732
