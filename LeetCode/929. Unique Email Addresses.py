import collections

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

# strip '.' from input string
# ignore all charactar after "+"
def reduce(s):
    s = s.replace(".", "")
    red = ""
    for c in s:
        if c == "+":
            break
        red += c
    return red


# use dictionary to avoid duplicate count
dict = collections.defaultdict(int)

# check each email in list
for email in emails:
    # split local name & domain name by '@'
    name = email.split('@')
    # reduce local name into a readable name
    reduceName = reduce(name[0]) + name[1]
    # add it to dictionary
    dict[reduceName] = 1

print(len(dict))