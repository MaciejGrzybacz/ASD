class UnionFind:
    # we are assuming that data is a list
    def __init__(self, data):
        self.data = data
        self.comp_sizes = [1 for _ in range(len(data))]
        self.ids = [i for i in range(len(data))]
        self.comp_count = len(data)

    def find(self, p):
        root = self.ids[p]
        while root != self.ids[root]:
            root = self.ids[root]

        while p != root:
            tmp = self.ids[p]
            self.ids[p] = root
            p = tmp

        return root

    def unify(self,p,q):
        proot = self.find(p)
        qroot = self.find(q)

        if proot == qroot:
            return

        if self.comp_sizes[proot] > self.comp_sizes[qroot]:
            self.comp_sizes[proot] += self.comp_sizes[qroot]
            self.comp_sizes[qroot] = 0
            self.ids[qroot] = proot
        else:
            self.comp_sizes[qroot] += self.comp_sizes[proot]
            self.comp_sizes[proot] = 0
            self.ids[proot] = qroot
        self.comp_count -= 1
