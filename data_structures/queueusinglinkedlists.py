from data_structures.LinkedLists import LinkedList
class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def __repr__(self):
        if self.queue.head is None:
            return f"Queue is empty Nothing to display"
        else:
            return f"Queue = {self.queue}"        

    def enqueue(self, val):
        self.queue.insertatend(val)

    def dequeue(self):
        if self.queue.head is None:
            raise IndexError("Queue is empty Nothing to remove")
        else:
            _,data = self.queue.removeatbeginning()
            return data

    def rear(self):
        if self.queue.head is None:
            print("Queue is empty Nothing in rear to display")
            return None
        else:
            rear = self.queue.lastelementinlinkedlist()
            return rear

    def front(self):
        if self.queue.head is None:
            print("Queue is empty Nothing in front to display")
            return None
        else:
            front = self.queue.firstelementinlinkedlist()
            return front

    def size(self):
        length = self.queue.lengthofthelinkedlist()
        return length

    def isEmpty(self):
        return self.queue.isEmptylinkedlist()

    def clear(self):
        self.queue.clear()