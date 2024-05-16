# implementation of doubly linked list


class DoublyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.prev = None
            self.next = None
            self.data = data

        def __str__(self):
            return str(self.data)

        def __repr__(self):
            return f"Node(data={self.data})"

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        tmp = self.head
        arr = []
        while tmp:
            arr.append(tmp.data)
            tmp = tmp.next
        return str(arr)

    def __iter__(self):
        self.current = self.head
        while self.current:
            yield self.current.data
            self.current = self.current.next

    def __list__(self):
        tmp = self.head
        arr = []
        while tmp:
            arr.append(tmp.data)
            tmp = tmp.next
        return arr

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        tmp = self.Node(data)
        if self.size == 0:
            self.tail = self.head = tmp
        else:
            self.tail.next = tmp
            tmp.prev = self.tail
            self.tail = self.tail.next
        self.size += 1

    def prepend(self, data):
        tmp = self.Node(data)
        if self.size == 0:
            self.tail = self.head = tmp
        self.head.prev = tmp
        tmp.next = self.head
        self.head = self.head.prev
        self.size += 1

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            raise ValueError('Node prev_node cannot be a None value!')
        if prev_node == self.tail:
            self.append(data)
        else:
            tmp = self.Node(data)
            tmp.next = prev_node.next
            tmp.prev = prev_node
            prev_node.next.prev = tmp
            prev_node.next = tmp
            self.size += 1

    def delete_node(self, key):
        tmp = self.find(key)
        if not tmp:
            raise ValueError('Key not found!')
        if tmp == self.head:
            if self.size > 1:
                tmp.next.prev = None
                self.head = tmp.next
            else:
                self.head = None
                self.tail=None
        elif tmp == self.tail:
            if self.size>1:
                tmp.prev.next = None
                self.tail = tmp.prev
            else:
                self.tail = None
                self.head=None
        else:
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
            tmp.prev = None
            tmp.next = None
        self.size -= 1

    def delete_node_at_position(self, position):
        if position < 0 or position >= self.size:  # we are counting from 0
            raise ValueError('Invalid position!')
        if position == 0:
            self.delete_node(self.head.data)
        elif position == self.size - 1:
            self.delete_node(self.tail.data)
        else:
            tmp = None
            if position > self.size // 2:
                tmp = self.tail
                for _ in range(self.size - 1, position - 1, -1):
                    tmp = tmp.prev
            else:
                tmp = self.head
                for _ in range(position + 1):
                    tmp = tmp.next

            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
            tmp.prev = None
            tmp.next = None

    def find(self, key):
        tmp = self.head
        while tmp:
            if tmp.data == key:
                return tmp
            tmp = tmp.next
        return None

    def reverse(self):
        tmp = self.head
        while tmp:
            tmp.next, tmp.prev = tmp.prev, tmp.next
            tmp = tmp.prev

        self.head, self.tail = self.tail, self.head
