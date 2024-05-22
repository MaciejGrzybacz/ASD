from data_structures.trees.binary_search_tree.bst import BST
import pytest

def test_add_valid_value():
    bst = BST()
    assert bst.add(5) == True
    assert bst.root.val == 5
    assert bst.size == 1

def test_remove_valid_value():
    bst = BST()
    bst.add(5)
    assert bst.remove(5) == True
    assert bst.root == None
    assert bst.size == 0

def test_find_valid_value():
    bst = BST()
    bst.add(5)
    assert bst.find(bst.root, 5) != None

def test_inorder_traversal(capsys):
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.intraverse(bst.root)
    captured = capsys.readouterr()
    assert captured.out == "3 5 7 "

def test_add_multiple_valid_values():
    bst = BST()
    assert bst.add(5) == True
    assert bst.add(3) == True
    assert bst.add(7) == True
    assert bst.root.val == 5
    assert bst.root.left.val == 3
    assert bst.root.right.val == 7
    assert bst.size == 3

def test_remove_leaf_node():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    assert bst.remove(3) == True
    assert bst.root.left == None
    assert bst.size == 2

def test_add_existing_value():
    bst = BST()
    bst.add(5)
    assert bst.add(5) == False

def test_remove_non_existing_value():
    bst = BST()
    bst.add(5)
    assert bst.remove(3) == False

def test_remove_from_empty_tree():
    bst = BST()
    assert bst.remove(5) == False

def test_traverse_empty_tree(capsys):
    bst = BST()
    bst.intraverse(bst.root)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_add_and_remove_same_value():
    bst = BST()
    assert bst.add(5) == True
    assert bst.add(5) == False
    assert bst.remove(5) == True
    assert bst.remove(5) == False

def test_remove_root_node():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.add(2)
    bst.add(4)
    bst.add(6)
    bst.add(8)
    bst.remove(5)
    assert bst.root.val == 6

def test_remove_node_with_one_child():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.add(2)
    bst.add(4)
    bst.add(6)
    bst.add(8)
    bst.remove(7)
    assert bst.find(bst.root, 7) is None
    assert bst.size == 6
    expected_order = [2, 3, 4, 5, 6, 8]
    assert bst.intraverse(bst.root) == expected_order

def test_add_and_remove_values():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.add(2)
    bst.add(4)
    bst.add(6)
    bst.add(8)
    assert bst.root.val == 5
    assert bst.root.left.val == 3
    assert bst.root.right.val == 7
    assert bst.root.left.left.val == 2
    assert bst.root.left.right.val == 4
    assert bst.root.right.left.val == 6
    assert bst.root.right.right.val == 8
    bst.remove(2)
    bst.remove(4)
    bst.remove(6)
    bst.remove(8)
    assert bst.root.val == 5
    assert bst.root.left.val == 3
    assert bst.root.right.val == 7
    assert bst.root.left.left is None
    assert bst.root.left.right is None
    assert bst.root.right.left is None
    assert bst.root.right.right is None

def test_remove_node_with_two_children():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.add(2)
    bst.add(4)
    bst.add(6)
    bst.add(8)
    assert bst.remove(3) == True
    assert bst.intraverse(bst.root) == [2, 4, 5, 6, 7, 8]

def test_remove_root_node_with_one_node():
    bst = BST()
    bst.add(5)
    assert bst.remove(5) == True
    assert bst.size == 0

def test_add_and_remove_values():
    bst = BST()
    assert bst.add(5) == True
    assert bst.add(3) == True
    assert bst.add(7) == True
    assert bst.add(2) == True
    assert bst.add(4) == True
    assert bst.add(6) == True
    assert bst.add(8) == True
    assert bst.find(bst.root, 5).val == 5
    assert bst.find(bst.root, 3).val == 3
    assert bst.find(bst.root, 7).val == 7
    assert bst.find(bst.root, 2).val == 2
    assert bst.find(bst.root, 4).val == 4
    assert bst.find(bst.root, 6).val == 6
    assert bst.find(bst.root, 8).val == 8
    assert bst.remove(2) == True
    assert bst.remove(4) == True
    assert bst.remove(6) == True
    assert bst.find(bst.root, 2) == None
    assert bst.find(bst.root, 4) == None
    assert bst.find(bst.root, 6) == None
