class HashTable:
    class Node:
        def __init__(self, key, val):
            self.next = None
            self.key = key
            self.val = val

    def __init__(self):
        self.size = 0
        self.capacity = 16
        self.max_load_factor = 0.5
        self.table = [None] * self.capacity

    def hash(self, key):
        # Using Python's built-in hash function ensures a more uniform distribution
        return key**2 % self.capacity

    def contains_key(self, key):
        return self.bucket_seek(self.hash(key), key) is not None

    def insert(self, key, val):
        if self.size / self.capacity >= self.max_load_factor:
            self.resize()
        self.bucket_insert(self.hash(key), self.Node(key, val))

    def get(self, key):
        node = self.bucket_seek(self.hash(key), key)
        if node is None:
            raise AttributeError(f'Key {key} does not exist!')
        return node.val

    def remove(self, key):
        self.bucket_remove(self.hash(key), key)

    def bucket_remove(self, index, key):
        prev = None
        curr = self.table[index]
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[index] = curr.next
                self.size -= 1
                return
            prev = curr
            curr = curr.next
        raise ValueError(f'Node with key of value {key} doesn\'t exist!')

    def bucket_insert(self, index, node):
        if not self.table[index]:
            self.table[index] = node
        else:
            curr = self.table[index]
            while curr:
                if curr.key == node.key:
                    raise ValueError(f'Key {node.key} already exists!')
                if not curr.next:
                    curr.next = node
                    break
                curr = curr.next
            else:
                curr.next = node
        self.size += 1

    def bucket_seek(self, index, key):
        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    def resize(self):
        old_capacity = self.capacity
        self.capacity *= 2
        new_table = [None] * self.capacity
        for i in range(old_capacity):
            curr = self.table[i]
            while curr:
                new_index = self.hash(curr.key)
                next_node = curr.next
                curr.next = new_table[new_index]
                new_table[new_index] = curr
                curr = next_node
        self.table = new_table

    def keys(self):
        kys = []
        for bucket in self.table:
            curr = bucket
            while curr:
                kys.append(curr.key)
                curr = curr.next
        return kys

    def values(self):
        vals = []
        for bucket in self.table:
            curr = bucket
            while curr:
                vals.append(curr.val)
                curr = curr.next
        return vals
