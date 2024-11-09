class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def reverseList(self, head):

    def create_linked_list(values):
        dummy = ListNode()
        current = dummy
        for val in values:
           current.next = ListNode(val)
           current = current.next
        return dummy.next
    def print_linked_list(head):
        values = []
        while head:
           values.append(str(head.val))
           head = head.next
        return " -> ".join(values)

head = create_linked_list([1, 2, 3, 4, 5, 6])
solution = Solution()
