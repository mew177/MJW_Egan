"""
            Question:
            1.

            Idea:
            1. Read the roman reversly
            2. if previous char is smaller or equal, that is to add it
            3. if provious char is larger, that is to minus it
            4. sum them
"""

s = 'III'

dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

pre_num = 0
value = 0

reverse = s[::-1]

for each in reverse:
    if pre_num <= dict[each]:
        value += dict[each]
    else:
        value -= dict[each]
    pre_num = dict[each]
print(value)