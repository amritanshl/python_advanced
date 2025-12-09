#enqueue(x), dequeue, peek, is_empty()
class Queue:
        def __init__(self):
            self.items = []
        def enqueue(self, item):
            self.items.append(item)
        def is_empty(self):
            return len(self.items) == 0
        def dequeue(self):
            if not self.is_empty():
                return self.items.pop(0) 
            return None
        def peek(self):
            if not self.is_empty():
                return self.items[0]
            return None
        def display(self):
             print("Queue: ", self.items)

print("\n====QUEUE IS QUEUING====")
queue = Queue()
queue.enqueue("Amrit")
queue.enqueue("Ankita")
queue.enqueue("debu")
queue.enqueue("Anjali")
queue.display()
queue.dequeue()
queue.display()
print("PEEK:  ", queue.peek())