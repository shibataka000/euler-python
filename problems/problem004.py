# coding: utf-8

import itertools


def is_palindromic_number(x):
    a = str(x)
    b = str(x)[::-1]
    return a == b


def solve():
    palindromic_numbers = []
    seq = range(100, 1000)
    for (a, b) in itertools.combinations(seq, 2):
        n = a * b
        if is_palindromic_number(n):
            palindromic_numbers.append(n)
    return max(palindromic_numbers)
