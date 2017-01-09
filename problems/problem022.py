# coding: utf-8


def read_data():
    with open("./problems/datas/problem022/names.txt") as f:
        raw = f.read().strip()
    names = [name.strip("\"") for name in raw.split(",")]
    names = sorted(names)
    return names


def get_score(name):
    return sum([ord(c) - ord("A") + 1 for c in name])


def solve():
    names = read_data()
    return sum([(i + 1) * get_score(name) for i, name in enumerate(names)])
