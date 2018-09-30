"""
    Question:
    1. How large would upper bound be?
    2. Are they able to be negative number?
    3.

    Idea:
    1. Go through every number. Terrible Time Complexity
"""

left = 1
right = 22

result = []

for num in range(left, right + 1):
    copy = str(num)
    is_dnum = True
    print(num)
    for n in copy:
        if n == "0":
            is_dnum = False
        elif num % int(n) != 0:
            is_dnum = False
        else:
            pass
    if is_dnum:
        result.append(num)

print(result)