
K = 4
S = "5F3Z-2e-9-w"

# strip all '-', reverse string and set all character to uppercase
S = S.replace("-", "")
S = S[::-1]
S = S.upper()

# group every four element and add to list
sp = [S[i * K:(i + 1) * K] for i in range(1 + len(S) // K)]
# join them with "-"
res = "-".join(sp)[::-1]

if len(res) == 0:
    print("")
elif res[0] == "-":
    print(res[1:len(res)])
else:
    print(res)

"""
    This innocently travel all element, BAD time complexity
"""
"""
S = S.replace("-", "")
res = ""
count = 0

for c in S[::-1]:    
    res += c.upper()    
    count += 1
    if count % K == 0:
        count = 0
        res += "-"


if len(res) <= 0:
    return ""
if res[len(res)-1] == "-":
    res = res[:len(res)-1]
return res[::-1]
"""