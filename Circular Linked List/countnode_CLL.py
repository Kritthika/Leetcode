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
        result =''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += '-->'
        return result
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length+=1

    def count_nodes(self):
        count = 0 
        temp = self.head
        while temp:
            count+=1
            temp = temp.next
            if temp == self.head:
                break
        return count
    
csllinked = CSLinkedList()
csllinked.append(10)
csllinked.append(20)
csllinked.append(30)
csllinked.append(40)

print(csllinked.count_nodes())

print(csllinked)

