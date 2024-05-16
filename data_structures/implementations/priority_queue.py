# implementation of heap-based minimum priority queue
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def shift_up(self, i):
        p = self.parent(i)
        while p >= 0 and self.heap[p] > self.heap[i]:
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            self.shift_up(p)

    def shift_down(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.size and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < self.size and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.shift_down(smallest)

    def push(self, data):
        self.heap.append(data)
        self.shift_up(self.size)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError('Empty queue!')
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_el = self.heap[-1]
        self.size -= 1
        self.heap=self.heap[:-1]
        self.shift_down(0)
        return min_el
