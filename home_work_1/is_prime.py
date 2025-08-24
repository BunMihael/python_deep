# ============================================================
# Assignment: Prime counter (Подсчёт простых)
# Description:
#   Read N integers from input and count how many of them are prime.
#   A prime is an integer >= 2 that has no divisors except 1 and itself.
#   Uses trial division up to sqrt(n) for efficiency.
# I/O:
#   In : N, then N lines with integers
#   Out: "Count of prime numbers: <value>"
# ============================================================

from math import isqrt
from typing import List


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    Prime numbers are >= 2 and divisible only by 1 and themselves.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def count_primes(numbers: List[int]) -> int:
    """Return how many prime numbers are in the list."""
    return sum(1 for n in numbers if is_prime(n))


def main() -> None:
    try:
        n = int(input("Enter how many numbers you will input: "))
        numbers = []

        for i in range(n):
            value = int(input(f"Enter number {i + 1}: "))
            numbers.append(value)

        result = count_primes(numbers)
        print(f"Count of prime numbers: {result}")

    except ValueError:
        print("Please enter valid integers only.")


if __name__ == "__main__":
    main()
