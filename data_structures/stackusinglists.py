from typing import Optional
class Stack:
    def __init__(self, maxSize:Optional[int]=0):
        self.stack = []
        self.stackSize = maxSize

    def __repr__(self):
        return f"Stack = {self.stack}"

    def push(self,val):
        is_dynamic = self.stackSize == 0
        if not is_dynamic and len(self.stack)>=self.stackSize:
            raise OverflowError("Stack Overflow")
        else:
            self.stack.append(val)

    def pop(self):
        if len(self.stack)>0:
            self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        return False if self.stack else True

    def size(self):
        return len(self.stack)

    def isFull(self):
        is_dynamic = self.stackSize == 0
        if not is_dynamic and len(self.stack)>=self.stackSize:
            return True
        else:
            return False

    def clear(self):
        self.stack.clear()