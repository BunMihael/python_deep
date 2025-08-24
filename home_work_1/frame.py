# ============================================================
# Task 1. Frame
# Write a program that draws a rectangular frame using
# character graphics. Use the vertical bar symbol (|) for vertical lines
# and the hyphen symbol (-) for horizontal lines. Let the user specify the width and
# height of the frame.
# ============================================================

# def draw_frame(width: int, height: int) -> None:
#     for i in range(height):
#         if i == 0 or i == height - 1:
#             spaces = '-' * (width - 2)
#         else:
#             spaces = ' ' * (width - 2)
#         print(f"|{spaces}|")
#
#
# def main():
#     try:
#         width = int(input("Write the number for the width of the rectangle:\n"))
#         height = int(input("Write the number for the hight of the rectangle:\n"))
#         if width <= 0 or height <= 0:
#             print("The number of rows must be greater than zero.\n")
#             return
#         draw_frame(width, height)
#
#     except ValueError:
#         print("Please enter an integer.\n")
#
#
# if __name__ == "__main__": main()

# ============================================================
# Assignment: Text Frame
# Description:
#   Draw a rectangular frame using ASCII characters.
#   Vertical edges use `v`, horizontal edges use `h`.
#   Width and height are provided by the caller/user.
# ============================================================

def make_frame(width: int, height: int, v: str = "|", h: str = "-", fill: str = " ") -> str:
    """
    Returns a rectangular frame as a single string with newlines.
    width, height  — inner dimensions in characters (>= 1).
    v, h           — symbols for vertical and horizontal edges.
    fill           — symbol for the inside area.
    """
    if width < 1 or height < 1:
        raise ValueError("width and height must be >= 1")

    # Top / bottom edges: h repeated `width` times, wrapped by verticals.
    top_bottom = f"{v}{h * width}{v}"

    # Middle line: fill inside, verticals on sides.
    middle = f"{v}{fill * width}{v}"

    # Build all lines: 1 top, (height-1) middle lines, 1 bottom
    lines = [top_bottom]
    for _ in range(height - 1):
        lines.append(middle)
    lines.append(top_bottom)

    return "\n".join(lines)


def main():
    try:
        w = int(input("Enter frame width: "))
        h = int(input("Enter frame height: "))
        print(make_frame(w, h))
    except ValueError:
        print("Please enter integers ≥ 1.")

if __name__ == "__main__":
    main()
