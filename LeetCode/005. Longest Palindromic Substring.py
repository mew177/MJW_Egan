"""
            Question:
            1. Is there a "" string input?
            2. Should I regard capital and small letter samely?
            3.

            Idea(innocent finding):
            1. Two for loop
            2. check each possible Palindromic str
            3. update whenever a longer Palindromic str is found

            TimeComplexity= O(n^3)

            Code:

            best = ""

            for i in range(len(s)):
                for j in range(i,len(s)+1):
                    temp = s[i:j]
                    if temp == temp[::-1]:
                        if len(temp) > len(best):
                            best = temp
            return best

        """

s = "aabcecbeaa"


def buildAround(s, L, R):
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1
    return R - L - 1


start = 0
end = 0

for i in range(len(s)):
    odd = buildAround(s, i, i)
    even = buildAround(s, i, i + 1)
    best = max(odd, even)
    if best > end - start:
        start = i - (best - 1) // 2
        end = i + best // 2

print(s[start:end + 1])
