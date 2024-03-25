class Stack:
    class Node:
        def __init__(self,data):
            self.next=None
            self.data=data
    def __init__(self):
        self.size = 0
        self.head=None

    def get_size(self):
        return self.size
    def push(self,data):
        if self.head is None:
            self.head=self.Node(data)
        else:
            tmp=self.head
            self.head=self.Node(data)
            self.head.next=tmp
        self.size+=1

    def pop(self):
        if self.head is None:
            raise IndexError("Empty stack!")

        tmp=self.head.data
        self.head=self.head.next
        self.size-=1
        return tmp
