class FenwickTree:
    def __init__(self, tree):
        self.tree = [0]
        self.tree.extend(tree)
        for i in range(1, len(self.tree)):
            lsb = self.lsb(i)
            if i + lsb < len(self.tree):
                self.tree[i + lsb] += self.tree[i]

    def lsb(self, i):
        return i & -i

    def prefix_sum(self, i):
        s = 0
        while i != 0:
            s += self.tree[i]
            i -= self.lsb(i)
        return s

    def sum(self, i, j):
        if i > j or i<1 or j>=len(self.tree):
            raise ValueError('Index error!')
        return self.prefix_sum(j) - self.prefix_sum(i - 1)

    def add(self, i, k):
        if i<0 or i>=len(self.tree):
           return
        while i < len(self.tree):
            self.tree[i] += k
            i += self.lsb(i)

    def set(self, i, k):
        if i<0 or i>=len(self.tree):
           return
        val = sum(i, i)
        self.add(i, k - val)
