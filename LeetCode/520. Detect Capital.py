# Beat 100% of people's code

"""
            Question:
            1. Will there be any charater other than alphebet
            2. How long will it possibily be?
            3. What type of input will it be?

            Idea:
            1. isupper() true, return true
            2. islower() true, return true
            3. word[1,len(word)] islower() true, return true
        """

word = "USA"
word2 = "Google"
word3 = "flaG"
word4 = "leetcode"

if word.isupper():
    print(True)
elif word.islower():
    print(True)
elif word[1:len(word)].islower():
    print(True)
else:
    print(False)