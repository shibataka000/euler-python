# coding: utf-8


def get_word(n):
    assert n > 0 and n <= 1000

    words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourtenn",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    if n in words:
        return words[n]
    elif n < 100 and n % 10 != 0:
        i = n % 10
        j = n - i
        return get_word(j) + "-" + get_word(i)
    elif n < 1000 and n % 100 == 0:
        i = round(n / 100)
        return get_word(i) + " hundred"
    elif n < 1000 and n % 100 != 0:
        i = n % 100
        j = n - i
        return get_word(j) + " and " + get_word(i)
    elif n == 1000:
        i = round(n / 1000)
        return get_word(i) + " thousand"


def solve():
    words = [get_word(i) for i in range(1, 1001)]
    words_len = [len(w.replace(" ", "").replace("-", "")) for w in words]
    return sum(words_len)
