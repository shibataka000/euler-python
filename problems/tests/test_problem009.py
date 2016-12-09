# coding: utf-8

import problems.problem009 as problem


def test_is_pythagoras_number():
    assert problem.is_pythagoras_number(3, 4, 5)
    assert problem.is_pythagoras_number(5, 4, 3)
    assert not problem.is_pythagoras_number(3, 4, 6)

    
def test_solve():
    assert problem.solve() == 31875000
