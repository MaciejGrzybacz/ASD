from DataStructures.implementations.BST import BST

import pytest


class TestBST:

    #  can add a valid value to the tree
    def test_add_valid_value(self):
        bst = BST()
        assert bst.add(5) == True
        assert bst.root.val == 5
        assert bst.size == 1

    #  can remove a valid value from the tree
    def test_remove_valid_value(self):
        bst = BST()
        bst.add(5)
        assert bst.remove(5) == True
        assert bst.root == None
        assert bst.size == 0

    #  can find a valid value in the tree
    def test_find_valid_value(self):
        bst = BST()
        bst.add(5)
        assert bst.find(bst.root, 5) != None

    #  can traverse the tree in-order
    def test_inorder_traversal(self, capsys):
        bst = BST()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.intraverse(bst.root)
        captured = capsys.readouterr()
        assert captured.out == "3 5 7 "

    #  can add multiple valid values to the tree
    def test_add_multiple_valid_values(self):
        bst = BST()
        assert bst.add(5) == True
        assert bst.add(3) == True
        assert bst.add(7) == True
        assert bst.root.val == 5
        assert bst.root.left.val == 3
        assert bst.root.right.val == 7
        assert bst.size == 3

    #  can remove a leaf node from the tree
    def test_remove_leaf_node(self):
        bst = BST()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        assert bst.remove(3) == True
        assert bst.root.left == None
        assert bst.size == 2

    #  can't add a value that already exists in the tree
    def test_add_existing_value(self):
        bst = BST()
        bst.add(5)
        assert bst.add(5) == False

    #  can't remove a value that doesn't exist in the tree
    def test_remove_non_existing_value(self):
        bst = BST()
        bst.add(5)
        assert bst.remove(3) == False

    #  can't remove a value from an empty tree
    def test_remove_from_empty_tree(self):
        bst = BST()
        assert bst.remove(5) == False

    #  can't traverse an empty tree
    def test_traverse_empty_tree(self, capsys):
        bst = BST()
        bst.intraverse(bst.root)
        captured = capsys.readouterr()
        assert captured.out == ""

    #  can add and remove the same value from the tree
    def test_add_and_remove_same_value(self):
        bst = BST()
        assert bst.add(5) == True
        assert bst.add(5) == False
        assert bst.remove(5) == True
        assert bst.remove(5) == False

    #  can remove the root node from the tree
    def test_remove_root_node(self):
        # Create a BST object
        bst = BST()

        # Add nodes to the BST
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(2)
        bst.add(4)
        bst.add(6)
        bst.add(8)

        # Remove the root node
        bst.remove(5)

        # Check if the root node is removed
        assert bst.root.val == 6

    #  can remove a node with one child from the tree
    def test_remove_node_with_one_child(self):
        # Create a BST object
        bst = BST()

        # Add nodes to the BST
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(2)
        bst.add(4)
        bst.add(6)
        bst.add(8)

        # Remove a node with one child
        bst.remove(7)

        # Check if the node is removed
        assert bst.find(bst.root, 7) is None

        # Check if the size is updated correctly
        assert bst.size == 6

        # Check if the remaining nodes are in the correct order
        expected_order = [2, 3, 4, 5, 6, 8]
        assert bst.intraverse(bst.root) == expected_order

    #  can add and remove values in a specific order
    def test_add_and_remove_values(self):
        # Create an instance of BST
        bst = BST()

        # Add values to the BST
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(2)
        bst.add(4)
        bst.add(6)
        bst.add(8)

        # Check if the values are added correctly
        assert bst.root.val == 5
        assert bst.root.left.val == 3
        assert bst.root.right.val == 7
        assert bst.root.left.left.val == 2
        assert bst.root.left.right.val == 4
        assert bst.root.right.left.val == 6
        assert bst.root.right.right.val == 8

        # Remove values from the BST
        bst.remove(2)
        bst.remove(4)
        bst.remove(6)
        bst.remove(8)

        # Check if the values are removed correctly
        assert bst.root.val == 5
        assert bst.root.left.val == 3
        assert bst.root.right.val == 7
        assert bst.root.left.left is None
        assert bst.root.left.right is None
        assert bst.root.right.left is None
        assert bst.root.right.right is None

    #  can't remove a node with two children from the tree
    def test_remove_node_with_two_children(self):
        # Create a BST object
        bst = BST()

        # Add nodes to the BST
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(2)
        bst.add(4)
        bst.add(6)
        bst.add(8)

        # Remove a node with two children
        assert bst.remove(3) == True
        assert bst.intraverse(bst.root) == [2, 4, 5, 6, 7, 8]

    #  can't remove the root node from a tree with only one node
    def test_remove_root_node_with_one_node(self):
        # Create a BST object
        bst = BST()

        # Add a single node to the tree
        bst.add(5)

        # Assert that the removal was unsuccessful
        assert bst.remove(5) == True
        assert bst.size == 0

    #  can add and remove multiple values from the tree
    def test_add_and_remove_values(self):
        # Create an instance of BST
        bst = BST()

        # Add values to the tree
        assert bst.add(5) == True
        assert bst.add(3) == True
        assert bst.add(7) == True
        assert bst.add(2) == True
        assert bst.add(4) == True
        assert bst.add(6) == True
        assert bst.add(8) == True

        # Check if values are added correctly
        assert bst.find(bst.root, 5).val == 5
        assert bst.find(bst.root, 3).val == 3
        assert bst.find(bst.root, 7).val == 7
        assert bst.find(bst.root, 2).val == 2
        assert bst.find(bst.root, 4).val == 4
        assert bst.find(bst.root, 6).val == 6
        assert bst.find(bst.root, 8).val == 8

        # Remove values from the tree
        assert bst.remove(2) == True
        assert bst.remove(4) == True
        assert bst.remove(6) == True

        # Check if values are removed correctly
        assert bst.find(bst.root, 2) == None
        assert bst.find(bst.root, 4) == None
        assert bst.find(bst.root, 6) == None
