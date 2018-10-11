"""
    Question:
    1. Is it possible to have more than one word occur the same time?
    2. Can 'a', 'the, 'it', etc, become a word?


    Idea:
    1. Use DefaultDict
    2. go throught each word and store them
    3. output max occurance word
"""

import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']

dict = collections.defaultdict(int)

word = ''
for char in paragraph:
    # parse character if its a alphabet
    if char.isalpha():
        word += char
    # parse until it meet a not letter character
    else:

        if len(word) > 0:
            # compare with banned list
            if word.lower() not in banned:
                # if it's not banned, dict[index] +1
                dict[word.lower()] += 1
        # go back again
        word = ''

# handling the last word is at last part of paragraph
if word != '' and word not in banned:
    dict[word.lower()] += 1

if len(dict) == 0:
    print ""
else:
    print (max(dict.items(), key=lambda a: a[1])[0])