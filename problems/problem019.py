# coding :utf-8


def is_uruu(year):
    if year % 400 != 0 and year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def get_days(year, month):
    if month == 2:
        return 29 if is_uruu(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def solve():
    date = 6  # 1900/12/01 is Saturday
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if month == 1:
                days = get_days(year - 1, 12)
            else:
                days = get_days(year, month - 1)
            date = (date + days) % 7
            if date == 0:
                sundays += 1
    return sundays
