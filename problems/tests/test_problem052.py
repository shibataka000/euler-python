# coding: utf-8

import problems.problem052 as problem


def test_is_permuted_multiples():
    assert problem.is_permuted_multiples(142857)
    assert not problem.is_permuted_multiples(142856)


def test_solve():
    assert problem.solve() == 142857
