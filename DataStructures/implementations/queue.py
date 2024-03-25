class Queue:
    class Node:
        def __init__(self, data):
            self.next = None
            self.data = data

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def dequeue(self):
        if self.size == 0:
            raise ValueError('Empty queue!')
        tmp = self.head.data
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return tmp

    def enqueue(self, data):
        if self.size == 0:
            self.head = self.tail = self.Node(data)
        else:
            self.tail.next = self.Node(data)
            self.tail = self.tail.next
        self.size += 1
