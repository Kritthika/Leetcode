class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.val)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def deleteDuplicates(self,head):
        if head is None:
            return None
        
        prev = None
        curr = head
        seen_vals = set()
        while curr:
            if curr.val in seen_vals:
                prev.next = curr.next
            else:
                seen_vals.add(curr.val)
                prev = curr
            curr = curr.next
        return head
new_linkedlist = Solution()
new_linkedlist.append(50)
new_linkedlist.append(30)
new_linkedlist.append(50)
new_linkedlist.append(20)
new_linkedlist.append(10)


print("Original Linked List:", new_linkedlist)
print("Length of Linked List:", new_linkedlist.length)

new_linkedlist.deleteDuplicates(new_linkedlist.head)
print("removed_duplicates Linked List:", new_linkedlist)
            