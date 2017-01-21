# coding: utf-8

import itertools
import math


def solve():
    ans = []
    for digits in itertools.combinations_with_replacement(range(10), 7):
        sum_of_factorial = sum([math.factorial(x) for x in digits if x != 0])
        for i in range(digits.count(0)):
            a = sum_of_factorial + i
            b = sum([math.factorial(int(x)) for x in str(a)])
            if a == b:
                ans.append(a)
    ans = list(set(ans))
    ans.remove(1)
    ans.remove(2)
    return sum(ans)
