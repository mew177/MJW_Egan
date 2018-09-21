s = "ab"

sub = ""
subList = [""]


for i in range(len(s)):
    same = False
    sub = ""
    for j in range(i, len(s)):
        for k in range(len(sub)):
            if s[j] == sub[k]:
                same = True
        if same:
            subList.append(sub)
            break
        else:
            sub = sub + s[j]
        if j == len(s)-1:
            subList.append(sub)

for key in range(len(subList)):
    subList[key] = len(subList[key])
print(subList)
