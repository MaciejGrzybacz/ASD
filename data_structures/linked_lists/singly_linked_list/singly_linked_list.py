class SinglyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.next = None
            self.data = data

        def __str__(self):
            return str(self.data)

        def __repr__(self):
            return f"Node(data={self.data})"

    def __init__(self):
        self.head = None
        self.tail = None
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
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def to_list(self):
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
            self.head = tmp
            self.tail = tmp
        else:
            self.tail.next = tmp
            self.tail = tmp
        self.size += 1

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise IndexError('Index out of range!')
        if index == 0:
            tmp = self.Node(data)
            tmp.next = self.head
            self.head = tmp
            self.size += 1
            return
        if index == self.size:
            self.append(data)
            return
        tmp = self.Node(data)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        tmp.next = curr.next
        curr.next = tmp
        self.size += 1

    def remove(self, data):
        if self.size == 0:
            raise ValueError('List is empty!')
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                if curr.next is None:
                    self.tail = curr
                self.size -= 1
                return
            curr = curr.next
        raise ValueError(f'Node with data of value {data} doesn\'t exist!')

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range!')
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next
        if curr.next is None:
            self.tail = curr
        self.size -= 1

    def find(self, data):
        curr = self.head
        index = 0
        while curr:
            if curr.data == data:
                return index
            curr = curr.next
            index += 1
        return -1

    def reverse(self):
        prev = None
        curr = self.head
        self.tail=self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
        self.tail.next = None
