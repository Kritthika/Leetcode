class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class CSLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result =''
        while temp_node is not None:
            result += str(temp_node.data)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += '-->'
        return result
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length+=1
    def is_sorted(self):
        if self.head is None or self.head.next == self.head:
            return True
        temp = self.head
        while temp.next != self.head:
            if temp.data > temp.next.data:
                return False
            temp = temp.next
        return True


csllinked = CSLinkedList()
csllinked.append(10)
csllinked.append(20)
csllinked.append(30)
csllinked.append(4)

print(csllinked)
print(csllinked.is_sorted())