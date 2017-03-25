# coding: utf-8


def solve():
    n = sum([i ** i for i in range(1, 1001)])
    return int(str(n)[-10:])
