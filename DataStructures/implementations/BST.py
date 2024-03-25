# implementation of BST which can contain only unique values
class BST:
    class Node:
        def __init__(self, left, right, val):
            self.left = left
            self.right = right
            self.val = val

    def __init__(self):
        self.root = None
        self.size = 0

    def find(self, node, val):
        if not node:
            return None
        elif node.val == val:
            return node
        elif node.val > val:
            return self.find(node.left, val)
        else:
            return self.find(node.right, val)

    def add(self, val):
        if self.find(self.root, val):
            return False  # we want to store unique values in tree

        self.root = self.add_helper(self.root, val)
        self.size += 1

        return True

    def add_helper(self, node, val):
        if not node:
            return self.Node(None, None, val)
        if node.val > val:
            return self.Node(self.add_helper(node.left, val), node.right, node.val)
        return self.Node(node.left, self.add_helper(node.right, val), node.val)

    def remove(self, val):
        if self.find(self.root, val):
            self.root = self.remove_helper(self.root, val)
            self.size -= 1
            return True
        return False

    def remove_helper(self, node, val):
        if not node:
            return None

        elif node.val > val:
            node.left = self.remove_helper(node.left, val)
        elif node.val < val:
            node.right = self.remove_helper(node.right, val)

        elif not node.left:
            return node.right

        elif not node.right:
            return node.left
        else:
            # we are searching for the smallest value on the right side
            tmp = node.right
            while tmp.left:
                tmp = tmp.left

            node.val = tmp.val
            node.right = self.remove_helper(node.right, tmp.val)

        return node

    # should print values in increasing order
    def intraverse(self, node, memo=None):
        if memo is None:
            memo = []
        if not node:
            return
        self.intraverse(node.left,memo)
        print(node.val, end=' ')
        memo.append(node.val)
        self.intraverse(node.right,memo)
        return memo
