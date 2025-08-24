# ============================================================
# Assignment: Sum of numbers
# Description:
#   From 1 to n=10, sum only even numbers not divisible by 3.
#   Result is printed at the end.
# ============================================================

n, e, i = 10, 3, 1
my_sum = 0
while i <= n:
    if i % 2 == 0:
        if i % e != 0:
            my_sum += i
    i += 1
print(f'Result = {my_sum}')
