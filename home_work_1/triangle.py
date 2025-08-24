from typing import Literal
from math import isclose

TriangleKind = Literal["equilateral", "isosceles", "scalene", "not a triangle"]


def triangle_type(a: float, b: float, c: float) -> TriangleKind:
    """
    Classify a triangle by its sides.
    Returns: "equilateral", "isosceles", "scalene", or "not a triangle".
    """
    a, b, c = sorted((a, b, c))

    if not a + b > c:
        return "not a triangle"

    if isclose(a, b) and isclose(b, c):
        return "equilateral"

    if isclose(a, b) or isclose(b, c) or isclose(a, c):
        return "isosceles"

    return "scalene"


def main():
    try:
        print("Set the length of the triangle sides.\n")
        a = float(input("Length of side a: "))
        b = float(input("Length of side b: "))
        c = float(input("Length of side c: "))
        result = triangle_type(a, b, c)
        print("Result:", result)
    except ValueError:
        print("Please enter valid numbers (≥ 0).")


if __name__ == "__main__":
    main()
