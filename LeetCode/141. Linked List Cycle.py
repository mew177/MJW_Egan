class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(5)

if head == None:
    print(False)

while True:
    if head.val == None:
        print(True)
    else:
        if head.next != None:
            head.val = None
            head = head.next
        else:
            print(False)