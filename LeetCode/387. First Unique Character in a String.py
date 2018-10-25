"""
            Question:
            1. Is capital the same with small letter
            2.

            Idea:
            1. Create a dictionary
            2. go through character and add count into dictionary
            3. tranverse again, and return then first character with count 1 in dictionary
            4. if there's not, then return -1
        """

import collections

s = "CreativeNinja"

if len(s) == 0:
    print(-1)
if len(s) == 1:
    print(0)

dict = collections.defaultdict(int)

for i in range(len(s)):
    dict[s[i]] += 1

for i in range(len(s)):
    if dict[s[i]] == 1:
        print(i)
print(-1)