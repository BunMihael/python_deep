# ============================================================
# Assignment: Guess my number (Компьютер угадывает число)
# Description:
#   Boy thinks of a number in [start, end]. Computer asks:
#   "Is your number equal / greater / less than N?"
#   Answers: 1 — equal, 2 — greater, 3 — less.
#   Deterministic mode uses binary search (≤ 7 tries for [1..100]).
#   Randomized mode resolves even ranges by probing mid or mid+1.
# I/O:
#   Interactive console dialogue.
# ============================================================

import random

CHOICES = {1: "equal", 2: "greater", 3: "less"}

def read_choice(n: int) -> int:
    while True:
        raw = input(
            f"Is your number {CHOICES[1]} / {CHOICES[2]} / {CHOICES[3]} than {n}? "
            "(enter 1=equal, 2=greater, 3=less): "
        ).strip()
        if raw in ("1", "2", "3"):
            return int(raw)
        print("Please enter only 1, 2 or 3.")

def guess_number_deterministic(start: int = 1, end: int = 100) -> None:
    if start > end:
        raise ValueError("start must be ≤ end")

    lo, hi = start, end
    count = 1
    print(f"Think of a number between {lo} and {hi}. I'll try to guess it.")

    while lo <= hi:
        mid = (lo + hi) // 2
        ans = read_choice(mid)

        if ans == 1:
            print(f"I guessed it in {count} attempts!")
            return
        elif ans == 2:
            lo = mid + 1
        else:
            hi = mid - 1
        count += 1

    print("Your answers were contradictory: the range became empty.")

def guess_number_randomized(start: int = 1, end: int = 100) -> None:
    if start > end:
        raise ValueError("start must be ≤ end")

    lo, hi = start, end
    count = 1
    print(f"Think of a number between {lo} and {hi}. I'll try to guess it.")

    while lo <= hi:
        mid = (lo + hi) // 2
        # if even range length, choose randomly between mid and mid+1
        if (hi - lo + 1) % 2 == 0:
            probe = random.choice((mid, mid + 1))
        else:
            probe = mid

        ans = read_choice(probe)

        if ans == 1:
            print(f"I guessed it in {count} attempts!")
            return
        elif ans == 2:
            lo = probe + 1
        else:
            hi = probe - 1
        count += 1

    print("Your answers were contradictory: the range became empty.")

def main() -> None:
    mode = input("Choose mode: 1 — deterministic, 2 — randomized: ").strip()
    if mode == "2":
        guess_number_randomized()
    else:
        guess_number_deterministic()

if __name__ == "__main__":
    main()
