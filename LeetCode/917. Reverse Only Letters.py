"""
            Question:
            1. What kind of ds is the input? String, char[], list?
            2. How large it might be?
            3. Will there be some special character like " / ...? How to solve it? Does it matter?

            Idea:
            1. Same idea as swifting all 1 to back, and 0 to front problem
            2. Set up two pointer start tranverse from left and right
            3. swich the value when they both meet a alphabet
            4. Tranverse untill they meet

            Time Complexity:
            O(n), n = number of character
"""

S = "Test1ng-Leet=code-Q!"
#output = "Qedo1ct-eeLg=ntse-T!"

lp = 0
rp = len(S) - 1
arr = list(S)

while lp < rp:
    while lp < rp:
        if not arr[lp].isalpha():
            lp += 1
        else:
            break
    while lp < rp:
        if not arr[rp].isalpha():
            rp -= 1
        else:
            break
    if arr[lp].isalpha() and arr[rp].isalpha():
        arr[lp], arr[rp] = arr[rp], arr[lp]
        lp += 1
        rp -= 1

print( ''.join(arr))