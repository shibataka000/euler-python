# coding: utf-8


def binary(n):
    return int(format(n, "b"))


def reverse(n):
    str_n = str(n)
    reversed_str_n = "".join(reversed(str_n))
    reversed_n = int(reversed_str_n)
    return reversed_n


def solve():
    return sum([i for i in range(1, 1000000, 2)
                if i == reverse(i)
                and binary(i) == reverse(binary(i))])
