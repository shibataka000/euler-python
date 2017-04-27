# coding: utf-8

import math

import math_ext


def solve():
    corners, primes = [], []
    for n in math_ext.corners():
        corners.append(n)
        if math_ext.is_prime(n):
            primes.append(n)
        if (len(corners) - 1) % 4 == 0 and len(corners) > 2:
            if len(primes) / len(corners) < 0.1:
                return math.floor((len(corners) + 2) / 4) * 2 + 1
