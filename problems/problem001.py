# coding: utf-8


def solve():
    ans = sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000)))
    return ans
