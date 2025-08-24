# ============================================================
# Assignment: Multiplication Table (Grouped by 4 columns)
# Description:
#   Print multiplication table from start×2 up to end×up_to
#   Split output into blocks of 4 columns (like in school).
# ============================================================

def print_multiplication_table(start: int = 2, end: int = 9, up_to: int = 10, block_size: int = 4) -> None:
    # calculate width for result alignment
    w_i   = len(str(end))
    w_j   = len(str(up_to))
    w_res = len(str(end * up_to))

    # helper function to format one multiplication expression
    def cell(i: int, j: int) -> str:
        return f"{i:>{w_i}} × {j:>{w_j}} = {i*j:>{w_res}}"

    # split into column blocks
    for block_start in range(start, end + 1, block_size):
        block_end = min(block_start + block_size - 1, end)

        # for each multiplier (rows)
        for j in range(2, up_to + 1):
            row = [cell(i, j) for i in range(block_start, block_end + 1)]
            print("   ".join(row))
        print()  # empty line between blocks


def main():
    print("Multiplication table from 2×2 up to 9×10 (4 columns per block):\n")
    print_multiplication_table()


if __name__ == "__main__":
    main()



# for k in [0, 4]:
#     for i in range(2, 11):
#         res = ''
#         for j in range(2 + k, 6 + k):
#             res += f'{j:^2} x {i:^2} = {i * j:^2}\t'
#         print(res)
#     print()