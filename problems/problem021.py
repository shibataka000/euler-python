# coding: utf-8

import math_ext


def get_amicable_number(a):
    def d(n):
        return sum(math_ext.get_true_divisors(n))

    b = d(a)
    if a == b or b == 0:
        return None
    elif a == d(b):
        return b
    else:
        return None


def solve():
    amicable_numbers = [get_amicable_number(i) for i in range(1, 10000)]
    amicable_numbers = [n for n in amicable_numbers if n is not None]
    return sum(amicable_numbers)
