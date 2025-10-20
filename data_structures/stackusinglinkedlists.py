from data_structures.LinkedLists import LinkedList
class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def __repr__(self):
        if self.stack.head is None:
            return f"Stack is empty Nothing to display"
        else:
            return f"Stack = {self.stack}"        

    def push(self,val):
        self.stack.insertatbeginning(val)

    def pop(self):
        if self.stack.head is None:
            return Exception("Stack is empty Nothing to remove")
        else:
            _,data = self.stack.removeatbeginning()
            return data

    def top(self):
        if self.stack.head is None:
            print("Stack is empty Nothing in top to display")
            return None
        else:
            peek = self.stack.firstelementinlinkedlist()
            return peek

    def size(self):
        length = self.stack.lengthofthelinkedlist()
        return length

    def isEmpty(self):
        return self.stack.isEmptylinkedlist()

    def clear(self):
        self.stack.clear()