# coding: utf-8


def pay(rest, coins):
    if rest == 0:
        yield []
    for i, coin in enumerate(coins):
        if coin <= rest:
            for p in pay(rest - coin, coins[i:]):
                yield [coin] + p


def solve():
    return len(list(pay(200, [200, 100, 50, 20, 10, 5, 2, 1])))
