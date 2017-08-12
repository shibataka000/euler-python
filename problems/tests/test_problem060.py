# coding: utf-8

import itertools

import problems.problem060 as problem


def test_is_prime_pair():
    for (p1, p2) in itertools.permutations([3, 7, 109, 673], 2):
        assert problem.is_prime_pair(p1, p2)
    assert not problem.is_prime_pair(2, 3)


def test_is_prime_pair_set():
    assert problem.is_prime_pair_set(3, (7, 109, 673))
    assert problem.is_prime_pair_set(7, (3, 109, 673))
    assert problem.is_prime_pair_set(109, (3, 7, 673))
    assert problem.is_prime_pair_set(673, (3, 7, 109))
    assert problem.is_prime_pair_set(3, ())
    assert not problem.is_prime_pair_set(2, (3,))


def test_solve():
    assert problem.solve() == 26033
