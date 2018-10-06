"""
    Question:
    1. Will there be empty matrix?
    2. Will there be character in matrix?
    3. What type is the input? Array?
    4.

    Idea:

    1. row size of Input, will be the column size of Output
    2. column size of Input, will be the row size of Output
    3. Output[y][x] = Input[x][y]

"""

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

row = len(A)
col = len(A[0])

trans = [[0 for _ in range(row)] for _ in range(col)]

for r in range(row):
    for c in range(col):
        trans[c][r] = A[r][c]

print(trans)