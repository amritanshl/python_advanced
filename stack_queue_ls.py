class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current = self.head
        while current.next:
            current=current.next
        current.next=new_node
    def prepend(self, data):
        new_node = Node(data)
        new_node.next=self.head
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")
    def delete(self,key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current:
            prev.next = current.next



print("=== Linked List Example ===")
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()   # 10 -> 20 -> 30 -> None

ll.prepend(5)
ll.display()   # 5 -> 10 -> 20 -> 30 -> None

ll.delete(20)
ll.display()   # 5 -> 10 -> 30 -> None

