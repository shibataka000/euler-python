# coding: utf-8

import problems.problem026 as problem


def test_get_repeating_decimal():
    assert problem.get_repeating_decimal_in_unit_fraction(2) == []
    assert problem.get_repeating_decimal_in_unit_fraction(3) == [3]
    assert problem.get_repeating_decimal_in_unit_fraction(4) == []
    assert problem.get_repeating_decimal_in_unit_fraction(5) == []
    assert problem.get_repeating_decimal_in_unit_fraction(6) == [6]
    assert problem.get_repeating_decimal_in_unit_fraction(7) == [
        1, 4, 2, 8, 5, 7
    ]
    assert problem.get_repeating_decimal_in_unit_fraction(8) == []
    assert problem.get_repeating_decimal_in_unit_fraction(9) == [1]
    assert problem.get_repeating_decimal_in_unit_fraction(10) == []


def test_solve():
    assert problem.solve() == 983
