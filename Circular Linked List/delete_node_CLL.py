class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1        
    
    def delete_by_value(self, value):
        if self.length == 0 :
            return False
        if self.head == self.tail and self.head.value == value:
            self.head = None
            self.tail = None
            self.length = 0
            return True
        prev = None
        current = self.head
        while True:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                    if current ==self.tail:
                        self.tail = prev
                
                self.length-=1
                return True
            prev = current
            current = current.next
            if current == self.head:
               break
        return False
csllinked = CSLinkedList()
csllinked.append(10)
csllinked.append(20)
csllinked.append(30)
csllinked.append(40)
csllinked.append(50)
print(csllinked)

print(csllinked.delete_by_value(30))
print(csllinked)

