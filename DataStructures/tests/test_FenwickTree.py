from DataStructures.implementations.fenwickTree import FenwickTree

import pytest

class TestFenwickTree:

    #  Initializing a FenwickTree object with a list of integers creates a tree with correct prefix sums
    def test_initialization_with_list(self):
        tree = [1, 2, 3, 4, 5]
        fenwick_tree = FenwickTree(tree)
        assert fenwick_tree.tree == [0, 1, 3, 3, 10, 5]

    #  Calling prefix_sum method with a valid index returns the correct prefix sum
    def test_prefix_sum_valid_index(self):
        tree = [1, 2, 3, 4, 5]
        fenwick_tree = FenwickTree(tree)
        assert fenwick_tree.prefix_sum(3) == 6

    #  Calling sum method with valid indices returns the correct sum
    def test_sum_valid_indices(self):
        tree = [1, 2, 3, 4, 5]
        fenwick_tree = FenwickTree(tree)
        assert fenwick_tree.sum(1, 3) == 6

       #  Initializing a FenwickTree object with an empty list creates a tree with only one element
    def test_initialization_with_empty_list(self):
        tree = []
        fenwick_tree = FenwickTree(tree)
        assert fenwick_tree.tree == [0]

    #  Calling sum method with invalid indices raises a ValueError
    def test_sum_invalid_indices(self):
        tree = [1, 2, 3, 4, 5]
        fenwick_tree = FenwickTree(tree)
        with pytest.raises(ValueError):
            fenwick_tree.sum(3, 1)

    #  Calling add method with an index outside the range of the tree does not update the tree
    def test_add_outside_range(self):
        tree = [1, 2, 3, 4, 5]
        fenwick_tree = FenwickTree(tree)
        fenwick_tree.add(6, 2)
        assert fenwick_tree.tree == [0, 1, 3, 3, 10, 5]

    #  Calling set method with an index outside the range of the tree does not update the tree
    def test_set_outside_range(self):
        tree = [1, 2, 3, 4, 5]
        fenwick_tree = FenwickTree(tree)
        fenwick_tree.set(6, 10)
        assert fenwick_tree.tree == [0, 1, 3, 3, 10, 5]

    #  Calling lsb method with a valid index returns the correct least significant bit
    def test_lsb_valid_index(self):
        tree = [1, 2, 3, 4, 5]
        fenwick_tree = FenwickTree(tree)
        assert fenwick_tree.lsb(5) == 1
