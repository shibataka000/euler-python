# coding: utf-8


def sum_of_each_digits(n):
    return sum([int(c) for c in str(n)])


def solve():
    return max([sum_of_each_digits(a ** b)
                for a in range(1, 100)
                for b in range(1, 100)])
