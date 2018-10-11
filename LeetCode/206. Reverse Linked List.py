class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# initialization
head = ListNode(1)

"""
            Question:
            1. Will this linked list always has a end?
            2. Which is better to implement in iteratively or recursively?
            3. 

            Idea:
            1. record previos node
            2. go to second node, and link it to previos node
            3. then record second node
            4. back to step 2.
            5. basis: link first node to None

            Time Complexity:
            O(n)
        """


def reverseNode(pre, post):
    record = post.next
    post.next = pre
    if record == None:
        return post
    else:
        return reverseNode(post, record)


if head == None:
    print(head)
elif head.next == None:
    print(head)
else:
    print(reverseNode(None, head))