# coding: utf-8

import math


def get_right_triangle_edges(p):
    return [(a, b, p - a - b)
            for a in range(math.floor(p / 3), math.ceil(p / 2))
            for b in range(math.floor((p - a) / 2), a + 1)
            if b >= p - a - b > 0 and
            a ** 2 == b ** 2 + (p - a - b) ** 2]


def solve():
    edges = {p: get_right_triangle_edges(p) for p in range(3, 1001)}
    return max(edges.items(), key=lambda x: len(x[1]))[0]
