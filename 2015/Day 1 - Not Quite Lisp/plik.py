result01 = 0
result02 = 1

for sign in open("./input-01.txt", "r").readline():
    if sign == ")":
        result01 -= 1
    else:
        result01 += 1
    if result01 < 0:
        break           
    result02 += 1

"""
Comment
    if result01 < 0:
            break           
        result02 += 1
If you want to see correct answer to first part
"""

print(result01, result02)