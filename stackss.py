#PUSH, POP, PEEK, IS_empty
class Stack:
    def __init__(self):
        self.items =[]
    def push(self,item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def display(self):
        print("Stack: ", self.items)

print("\n====STACK IS STACKING====")
stack = Stack()
stack.push("Ankita")
stack.push("Debu")
stack.push("Mahi")
stack.push("Amrit")

stack.display()
stack.pop()

print("Peek: ", stack.peek())
