# coding: utf-8

import problems.problem035 as problem


def test_get_circular_number():
    assert problem.get_circular_numbers(2) == [2]
    assert problem.get_circular_numbers(11) == [11, 11]
    assert problem.get_circular_numbers(197) == [197, 971, 719]


def test_is_circular_prime():
    assert problem.is_circular_prime(2)
    assert problem.is_circular_prime(11)
    assert problem.is_circular_prime(197)
    assert problem.is_circular_prime(971)
    assert problem.is_circular_prime(719)
    assert not problem.is_circular_prime(19)


def test_solve():
    assert problem.solve() == 55
