# coding: utf-8

import itertools

import math_ext


def abundant_number():
    i = 1
    while True:
        divisors = math_ext.get_true_divisors(i)
        if sum(divisors) > i:
            yield i
        i += 1


def solve():
    abundant_number_list = itertools.takewhile(
        lambda x: x <= 28123, abundant_number()
    )
    L = [a + b for (a, b) in itertools.product(abundant_number_list, repeat=2)]
    return sum(set(range(1, 28124)) - set(L))
