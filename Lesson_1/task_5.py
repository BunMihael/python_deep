# ============================================================
# Assignment: Number transformation
# Description:
#   Input: integer from 1 to 999.
#   - If 1 digit → square it
#   - If 2 digits → multiply digits
#   - If 3 digits → reverse digits
#   Else: print "Out of range"
# ============================================================

def draw_tree(rows: int, figure: str) -> None:
    for i in range(1, rows + 1):
        start = ' ' * (rows - i)
        stars = figure * (2 * i - 1)
        print(start + stars)


def main():
    try:
        rows = int(input("How many rows should a Christmas tree have?\n"))
        figure = input("Enter a simbol for a tree\n")
        if rows <= 0:
            print("The number of rows must be greater than zero.\n")
            return
        draw_tree(rows, figure)
    except ValueError:
        print("Please enter an integer.\n")


if __name__ == "__main__": main()
