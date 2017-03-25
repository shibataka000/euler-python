# coding: utf-8

import problems.problem049 as problem


def test_get_4_digit_primes():
    primes = problem.get_4_digit_primes()
    assert all([len(str(n)) == 4 for n in primes])


def test_filter_permutations():
    def filter_permutations(elem, seq):
        return list(problem.filter_permutations(elem, seq))

    assert filter_permutations(12, [12, 13, 21]) == [12, 21]
    assert filter_permutations(112, [121, 122]) == [121]
    assert filter_permutations(12, [1122]) == []


def test_find_3_elem_arithmetic_sequence():
    assert problem.find_3_elem_arithmetic_sequence(
        [1487, 1847, 4817, 4871, 7481, 7841, 8147, 8741]
    ) == [1487, 4817, 8147]


def test_solve():
    assert problem.solve() == 296962999629
