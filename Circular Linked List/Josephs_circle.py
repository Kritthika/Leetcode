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
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def count_nodes(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def delete_node(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        temp = self.head
        while self.count_nodes() > 1:
            count = 1
            while count != step:
                temp = temp.next
                count+=1
            self.delete_node(temp.data)
            print(f"removed {temp.data}")
            temp = temp.next


        return f"Last person left standing: {temp.data}"
csllinked = CircularLinkedList()
csllinked.append(10)
csllinked.append(20)
csllinked.append(30)
csllinked.append(40)
csllinked.append(50)

print(csllinked)
print(csllinked.josephus_circle(1))