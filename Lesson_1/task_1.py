# ============================================================
# Assignment: Quadratic equation
# Description:
#   Solve equation 5x² - 10x - 400 = 0.
#   Uses discriminant (b² - 4ac) to check number of roots.
# ============================================================

from math import sqrt

# Коофициент уровнения 5x^2 -10x - 400 = 0
a, b, c = 5, -10, -400

d = b ** 2 - 4 * a * c
if d < 0:
    print("Корней нет")
if d == 0:
    x = -b / (2 * a)
    print(f"Один корень: x = {x}")
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f"Два корня: x1 = {x1}, x2 = {x2}")
