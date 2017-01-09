# coding: utf-8


def get_repeating_decimal_in_unit_fraction(b):
    a = 1
    div_list = []
    while True:
        a *= 10
        reminder = a % b
        product = a // b
        if reminder == 0:
            return []
        elem = (product, reminder)
        if elem in div_list:
            i = div_list.index(elem)
            return [p for (p, r) in div_list[i:]]
        div_list.append(elem)
        a = reminder


def solve():
    repeating_decimals = [
        (i, get_repeating_decimal_in_unit_fraction(i))
        for i in range(1, 1000)
    ]
    return max(repeating_decimals, key=lambda x: len(x[1]))[0]
