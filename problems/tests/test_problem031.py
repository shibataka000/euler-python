# coding: utf-8

import problems.problem031 as problem


def test_pay():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    assert list(problem.pay(1, coins)) == [[1]]
    assert list(problem.pay(2, coins)) == [[2], [1, 1]]
    assert list(problem.pay(3, coins)) == [[2, 1], [1, 1, 1]]
    assert list(problem.pay(4, coins)) == [
        [2, 2], [2, 1, 1], [1, 1, 1, 1]
    ]


def test_solve():
    assert problem.solve() == 73682
