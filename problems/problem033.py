# coding: utf-8

from fractions import Fraction


def solve():
    ans = Fraction(1, 1)
    for a in range(11, 100):
        if a % 10 == 0:
            continue
        for b in range(a + 1, 100):
            if b % 10 == 0:
                continue
            a_str = str(a)
            b_str = str(b)
            for i in range(2):
                for j in range(2):
                    if a_str[i] == b_str[j]:
                        a2 = int(a_str[(i + 1) % 2])
                        b2 = int(b_str[(j + 1) % 2])
                        f1 = Fraction(a, b)
                        f2 = Fraction(a2, b2)
                        if f1 == f2:
                            ans *= f1
    return ans.denominator
