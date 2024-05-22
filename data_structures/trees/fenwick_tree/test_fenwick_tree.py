import pytest
from data_structures.trees.fenwick_tree.fenwick_tree import FenwickTree

def test_initialization_with_list():
    tree = [1, 2, 3, 4, 5]
    fenwick_tree = FenwickTree(tree)
    assert fenwick_tree.tree == [0, 1, 3, 3, 10, 5]

def test_prefix_sum_valid_index():
    tree = [1, 2, 3, 4, 5]
    fenwick_tree = FenwickTree(tree)
    assert fenwick_tree.prefix_sum(3) == 6

def test_sum_valid_indices():
    tree = [1, 2, 3, 4, 5]
    fenwick_tree = FenwickTree(tree)
    assert fenwick_tree.sum(1, 3) == 6

def test_initialization_with_empty_list():
    tree = []
    fenwick_tree = FenwickTree(tree)
    assert fenwick_tree.tree == [0]

def test_sum_invalid_indices():
    tree = [1, 2, 3, 4, 5]
    fenwick_tree = FenwickTree(tree)
    with pytest.raises(ValueError):
        fenwick_tree.sum(3, 1)

def test_add_outside_range():
    tree = [1, 2, 3, 4, 5]
    fenwick_tree = FenwickTree(tree)
    fenwick_tree.add(6, 2)
    assert fenwick_tree.tree == [0, 1, 3, 3, 10, 5]

def test_set_outside_range():
    tree = [1, 2, 3, 4, 5]
    fenwick_tree = FenwickTree(tree)
    fenwick_tree.set(6, 10)
    assert fenwick_tree.tree == [0, 1, 3, 3, 10, 5]

def test_lsb_valid_index():
    tree = [1, 2, 3, 4, 5]
    fenwick_tree = FenwickTree(tree)
    assert fenwick_tree.lsb(5) == 1
