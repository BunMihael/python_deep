# ============================================================
# Assignment: Number transformation
# Description:
#   Input: integer from 1 to 999.
#   - If 1 digit → square it
#   - If 2 digits → multiply digits
#   - If 3 digits → reverse digits
#   Else: print "Out of range"
# ============================================================

num = int(input("Write number from 1 to 999\n"))
digits = len(str(num))
if digits == 1:
    result = num ** 2
elif digits == 2:
    d1, d2 = divmod(num, 10)
    result = d1 * d2
elif digits == 3:
    result = int(str(num)[::-1])
else:
    result = "Out of range"
print("Result:", result)

# num = input("Write number from 1 to 999\n")
# if not num.isdigit() or not (1 <= int(num) <= 999):
#     result = "Out of range"
# else:
#     if len(num) == 1:
#         result = int(num) ** 2
#     elif len(num) == 2:
#         result = int(num[0]) * int(num[1])
#     else:
#         result = int(num[::-1])
# print("Result:", result)
#
# num = int(input("Write number from 1 to 999\n"))
#
# digits = 0
# temp = num
# while temp > 0:
#     temp //= 10
#     digits += 1
# if digits == 1:
#     result = num ** 2
# elif digits == 2:
#     d1 = num // 10
#     d2 = num % 10
#     result = d1 * d2
# elif digits == 3:
#     d1 = num // 100
#     d2 = (num // 10) % 10
#     d3 = num % 10
#     result = d3 * 100 + d2 * 10 + d1
# else:
#     result = "Out of range"
# print("Result:", result)
