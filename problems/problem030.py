# coding: utf-8


def get_value(n):
    return sum([int(x) ** 5 for x in str(n)])


def solve():
    m = get_value(999999)
    return sum([n for n in range(2, m) if get_value(n) == n])
