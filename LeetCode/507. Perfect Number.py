"""
    Question:
    1. How large will the number possible be?
    2. Is 1 a perfect number?
    3.

    Idea:
    1. Check dividers less than sqrt(num),
    2. sum their prime dividers and (num / prime divider). (Terrible Time Complexity?)

"""

num = 28

if num <= 1:
    print(False)
s = 1
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        s += i
        s += num // i
print(num == s)