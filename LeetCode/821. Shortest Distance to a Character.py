"""
            Question:
            1. Is capital letter the same with little character?
            2. Will there be empty input? or empty C?
            3.

            Idea(wrong):
            1. create a same size array
            2. tranverse from 0 to n (as i)
            3. let ls(left start) = 0
            4. when S[i] != C, List[ls:i] + 1
            5. if S[i] == C, ls = i, return to step 4

            Time Complexity:
            O(n + n!), n = first loop tranverse, n! = add 1 for every time


            Idea:
            1. find all index of C
            2. go through S again
            3. and choose the distance will each index of C

            Time Complexity:
            O(n + nm), n = find index of C, m = number of index, n = len(S)

"""

S = "loveleetcode"
C = 'e'

count = [0 for _ in range(len(S))]
indecies = []

for i in range(len(S)):
    if S[i] == C:
        indecies.append(i)

for i in range(len(S)):
    count[i] = min([abs(k - i) for k in indecies])
print(count)
