class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
        curr = curr.next
        return dummy.next



head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]