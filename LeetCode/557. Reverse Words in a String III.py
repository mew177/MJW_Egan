"""
            Question:
            1. Will there be ',' in the string?
            2. What's the maximum size of the string?
            3. Should I return in the same string?


            Idea:
            1. Split them into list with ' '
            2. use the same idea of left pointer and right pointer
            3. go through each word
            4. concatinate them back with ' '
        """

s = "Let's take LeetCode contest"

s = s.split(" ")


def reverse(word):
    lp = 0
    rp = len(word) - 1

    word = list(word)

    while lp < rp:
        word[lp], word[rp] = word[rp], word[lp]
        lp += 1
        rp -= 1

    return ''.join(word)


for i in range(len(s)):
    s[i] = reverse(s[i])

print(' '.join(s))