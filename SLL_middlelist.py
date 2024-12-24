class ListNode(object):
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next
class Solution(object):
    def findmiddle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
head =  ListNode(2, ListNode(3, ListNode(4, ListNode(5))))

# Find the middle
solution = Solution()
middle = solution.findmiddle(head)

print("Middle node value:", middle.val)
        