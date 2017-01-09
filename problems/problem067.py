# coding: utf-8

from . import problem018


def solve():
    with open("./problems/datas/problem067_triangle.txt") as f:
        triangle = f.read()
    return problem018.get_max_route_value(triangle)
