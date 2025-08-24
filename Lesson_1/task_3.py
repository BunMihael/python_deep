# ============================================================
# Assignment: Leap year check
# Description:
#   Return 'Yes' if given year is leap, else 'No'.
#   Rule: divisible by 400 OR divisible by 4 but not by 100.
# ============================================================

def func(year):
    return 'Yes' if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 'No'


print(func(2024))
