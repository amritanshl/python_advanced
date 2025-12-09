#Linked List
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    #O(n)
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

        #O(1)
        #head->10->20->30->None  + 70
         #head->70->10->20->30->None 
    def prepend(self, data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def display(self):
        current=self.head
        while current:
            print(current.data, end = ' => ')
            current=current.next
        print("None")

    def insert_at_index(self, index, data):
        if index == 0:
            new_node = Node(data)
            new_node.next=self.head
            self.head=new_node
            return
        current=self.head
        current_index=0
        while current and current_index < index-1:
            current=current.next
            current_index+=1
        
        if current is None:
            return

        new_node.next = current.next
        current.next=new_node
    def delete(self, key):
        current = self.head
        if current and current.data==key:
            self.head=current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current:
            prev.next = current.next


    
# my_list = LinkedList()
# my_list.append("Ankita")
# my_list.append("Debu")
# my_list.append("Parminder")
# my_list.append("Amrit")
# my_list.prepend("Thriveni")
# my_list.display()
