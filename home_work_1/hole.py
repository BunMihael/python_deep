# ============================================================
# Assignment: Pit (Яма)
# Description:
#   Build a numeric "pit" of given depth. Each line has:
#   - descending numbers on the left
#   - dots in the middle
#   - ascending numbers on the right
#   Return the whole figure as a single string (for tests/printing).
# ============================================================

from typing import Iterable

def build_pit(depth: int, dot: str = ".") -> str:
    """
    Return the pit as a single string with newlines.
    :param depth: pit depth (>=1)
    :param dot:   filler between left/right parts (default '.')
    """
    if depth < 1:
        raise ValueError("depth must be >= 1")
    if len(dot) != 1:
        raise ValueError("dot must be a single character")

    lines: list[str] = []

    for line in range(depth):
        # left: depth, depth-1, ..., depth-line
        left: str = "".join(str(x) for x in range(depth, depth - line - 1, -1))
        # middle: dots count = 2 * (depth - line - 1)
        mid_count: int = 2 * (depth - line - 1)
        middle: str = dot * mid_count
        # right: depth-line, ..., depth
        right: str = "".join(str(x) for x in range(depth - line, depth + 1))

        lines.append(left + middle + right)

    return "\n".join(lines)


def main() -> None:
    try:
        depth = int(input("Enter pit depth: "))
        print(build_pit(depth))
    except ValueError as e:
        print(f"Input error: {e}")


if __name__ == "__main__":
    main()
