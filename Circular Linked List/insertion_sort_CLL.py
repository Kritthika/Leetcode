class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
     
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
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    def insert_into_sorted(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
        if data < self.head.data:
            self.prepend(data)
            return
        temp = self.head
        while temp.next != self.head and temp.next.data < data:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
csllinked = CircularLinkedList()
csllinked.append(10)
csllinked.append(20)
csllinked.append(30)
csllinked.append(40)

print(csllinked)
insert=csllinked.insert_into_sorted(33)
print(csllinked)
