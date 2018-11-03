"""
            Question:
            1. how long can the string be?
            2. Is there going to be more than one '*' but should be regarded differently?

            Idea:
            1. stack
            2. start from left
            3. push '('
            4. pop one '(' when meet a ')'
            5. when meet '*' push [treat it as '(']
                5.1 if works, that means '*' is treated as '('
                5.2 if not, go from right to left
            6. when meet '*' push [treat it as ')']
                5.1 if works, that means '*' is treated as ')'
                5.2 if not, that means '*' treated as " "

            Time Complexity: O(n)
        """
s = "(*))"


stack = []

# parse character from left to right
for p in s:
    # push '(' '*'
    if p == '(' or p == '*':
        stack.append(p)
    else:
        # if there's '*' ')' in stack, pop one out
        if len(stack) > 0:
            stack.pop(0)
        # if nothing is in stack, that means # of right and left parenthesis is not the same
        else:
            print("False")

stack = []
# parse character from right to left
for p in s[::-1]:
    # push ')'
    if p == ')' or p == '*':
        stack.append(p)
    else:
        # if there's '(' in stack, pop one out
        if len(stack) > 0:
            stack.pop(0)
        # if nothing is in stack, that means # of right and left parenthesis is not the same
        else:
            print("False")

print("True")