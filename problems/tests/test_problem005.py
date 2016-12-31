# coding: utf-8

import problems.problem005 as problem


def test_gcd():
    assert problem.gcd(2, 1) == 1
    assert problem.gcd(2, 2) == 2
    assert problem.gcd(2, 3) == 1
    assert problem.gcd(2, 4) == 2


def test_lcm():
    assert problem.lcm(2, 3) == 6
    assert problem.lcm(2, 4) == 4


def test_solve():
    assert problem.solve() == 232792560
