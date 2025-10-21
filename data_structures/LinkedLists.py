class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        temp = self.head
        while temp is not None:
            nodes.append(str(temp.data))
            temp = temp.next
        return "->".join(nodes)+"-> None"

    def insertatbeginning(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        return self.head

    def insertatend(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            node = Node(data)
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        return self.head

    def removeatbeginning(self):
        if self.head is None:
            return None

        elif self.head.next is None:
            temp = self.head.data
            self.head = None
            return self.head,temp

        else:
            temp = self.head.data
            self.head = self.head.next
            return self.head,temp

    def firstelementinlinkedlist(self):
        if self.head is None:
            return None

        elif self.head.next is None:
            return self.head.data

        else:
            temp = self.head
            return temp.data

    def lastelementinlinkedlist(self):
        if self.head is None:
            return None

        elif self.head.next is None:
            return self.head.data

        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            return temp.data

    def lengthofthelinkedlist(self):
        cnt = 0
        temp = self.head
        while temp is not None:
            cnt+=1
            temp = temp.next
        return cnt

    def isEmptylinkedlist(self):
        return True if self.head is None else False

    def clear(self):
        self.head = None