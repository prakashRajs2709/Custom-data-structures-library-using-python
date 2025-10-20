from typing import Optional
class Queue:
    def __init__(self, maxSize:Optional[int]=0):
        self.qsize = maxSize
        self.queue = []

    def __repr__(self):
        return f"Queue = {self.queue}"

    def enqueue(self,val):
        is_dynamic = self.qsize == 0
        if not is_dynamic and len(self.queue)>=self.qsize:
            raise OverflowError("Queue Overflow")
        else:
            self.queue.append(val)

    def dequeue(self):
        if len(self.queue)>0:
            self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def rear(self):
        return self.queue[-1]

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return False if self.queue else True

    def isFull(self):
        is_dynamic = self.qsize == 0
        if not is_dynamic and len(self.queue)>=self.qsize:
            return True
        else:
            return False

    def clear(self):
        self.queue.clear()