# I'm using Python list like static array to implement own dynamic array, ignoring it's capabilities
class DynamicArray:
    def __init__(self):
        self.arr = [None] * 16
        self.size = 0
        self.capacity = 16

    def __iter__(self):
        return iter(self.arr[:self.size])

    def __len__(self):
        return self.size

    def append(self, data):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        if self.size < self.capacity:
            self.arr[self.size] = data
            self.size += 1

    def resize(self, new_capacity):
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def remove(self, data):
        index = self.arr.index(data)
        if index == -1:
            raise ValueError('There is no ' + data + ' in array!')
        for i in range(index + 1, self.size):
            self.arr[i - 1] = self.arr[i]
        self.size -= 1
        self.arr[self.size] = None
        if self.size * 2 < self.capacity:
            self.resize(self.capacity//2)

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise IndexError('Index out of range!')
        if index == self.size:
            self.append(data)
            return
        temp = self.arr[self.size - 1]
        for i in range(index + 1, self.size):
            self.arr[i] = self.arr[i - 1]
        self.append(temp)
        self.arr[index] = data
