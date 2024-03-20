
from DataStructures.implementations.doublyLinkedList import DoublyLinkedList

import pytest

class TestDoublyLinkedList:

    #  create an empty DoublyLinkedList and check that its size is 0
    def test_empty_list_size(self):
        dll = DoublyLinkedList()
        assert len(dll) == 0

    #  append an element to a DoublyLinkedList and check that its size increased by 1
    def test_append_element(self):
        dll = DoublyLinkedList()
        dll.append(1)
        assert len(dll) == 1

    #  prepend an element to a DoublyLinkedList and check that its size increased by 1
    def test_prepend_element(self):
        dll = DoublyLinkedList()
        dll.prepend(1)
        assert len(dll) == 1

    #  insert an element after a node in a DoublyLinkedList and check that its size increased by 1
    def test_insert_after_node(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.insert_after_node(dll.head, 2)
        assert len(dll) == 2

    #  delete a node from a DoublyLinkedList and check that its size decreased by 1
    def test_delete_node(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.delete_node(1)
        assert dll.head == None
        assert dll.tail == None
        assert len(dll) == 0


    #  delete the first node from a DoublyLinkedList and check that its size decreased by 1
    def test_delete_first_node(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.delete_node(1)
        assert len(dll) == 1

    #  try to delete a node from an empty DoublyLinkedList and check that a ValueError is raised
    def test_delete_node_empty_list(self):
        dll = DoublyLinkedList()
        with pytest.raises(ValueError):
            dll.delete_node(1)

    #  try to insert an element after a None node in a DoublyLinkedList and check that a ValueError is raised
    def test_insert_after_none_node(self):
        dll = DoublyLinkedList()
        with pytest.raises(ValueError):
            dll.insert_after_node(None, 1)

    #  try to delete a node with a key that does not exist in a DoublyLinkedList and check that a ValueError is raised
    def test_delete_node_key_not_found(self):
        dll = DoublyLinkedList()
        dll.append(1)
        with pytest.raises(ValueError):
            dll.delete_node(2)

    #  try to delete a node at a position that does not exist in a DoublyLinkedList and check that a ValueError is raised
    def test_delete_node_invalid_position(self):
        dll = DoublyLinkedList()
        dll.append(1)
        with pytest.raises(ValueError):
            dll.delete_node_at_position(1)

    #  try to delete a node at position 0 in a DoublyLinkedList with size 1 and check that the DoublyLinkedList becomes empty
    def test_delete_node_position_0_size_1(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.delete_node_at_position(0)
        assert len(dll) == 0

    #  try to delete a node at the last position in a DoublyLinkedList with size 1 and check that the DoublyLinkedList becomes empty
    def test_delete_node_last_position_size_1(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.delete_node_at_position(0)
        assert len(dll) == 0

    #  delete the last node from a DoublyLinkedList and check that its size decreased by 1
    def test_delete_last_node_size_decreased(self):
        # Create a DoublyLinkedList object
        dll = DoublyLinkedList()

        # Append nodes to the list
        dll.append(1)
        dll.append(2)
        dll.append(3)

        # Delete the last node
        dll.delete_node(3)

        # Check that the size decreased by 1
        assert len(dll) == 2

    #  reverse a DoublyLinkedList and check that its elements are in reverse order
    def test_reverse_doubly_linked_list(self):
        # Create a DoublyLinkedList object
        dll = DoublyLinkedList()

        # Append elements to the list
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.append(4)
        dll.append(5)

        # Reverse the list
        dll.reverse()

        # Check that the elements are in reverse order
        assert list(dll) == [5, 4, 3, 2, 1]

    #  insert an element after the first node in a DoublyLinkedList and check that its size increased by 1
    def test_insert_after_first_node_size_increased(self):
        # Create a DoublyLinkedList object
        dll = DoublyLinkedList()

        # Append elements to the list
        dll.append(1)
        dll.append(2)
        dll.append(3)

        # Insert an element after the first node
        dll.insert_after_node(dll.head, 4)

        # Check that the size increased by 1
        assert len(dll) == 4

    #  create a DoublyLinkedList with multiple elements and check that its size is correct
    def test_create_doubly_linked_list_with_multiple_elements(self):
        # Create a DoublyLinkedList
        dll = DoublyLinkedList()

        # Append elements to the DoublyLinkedList
        dll.append(1)
        dll.append(2)
        dll.append(3)

        # Check that the size of the DoublyLinkedList is correct
        assert len(dll) == 3

    #  insert an element after a middle node in a DoublyLinkedList and check that its size increased by 1
    def test_insert_after_middle_node_size_increased(self):
        # Create a DoublyLinkedList object
        dll = DoublyLinkedList()

        # Append elements to the list
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.append(4)

        # Insert an element after the middle node
        dll.insert_after_node(dll.head.next, 5)

        # Check that the size increased by 1
        assert len(dll) == 5

    #  insert an element after the last node in a DoublyLinkedList and check that its size increased by 1
    def test_insert_after_last_node(self):
        # Create a DoublyLinkedList object
        dll = DoublyLinkedList()

        # Append some elements to the list
        dll.append(1)
        dll.append(2)
        dll.append(3)

        # Get the initial size of the list
        initial_size = len(dll)

        # Insert an element after the last node
        dll.insert_after_node(dll.tail, 4)

        # Check that the size increased by 1
        assert len(dll) == initial_size + 1

    #  delete a node from a DoublyLinkedList with multiple elements and check that its size decreased by 1
    def test_delete_node_size_decrease(self):
        # Create a DoublyLinkedList with multiple elements
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.append(4)
        dll.append(5)

        # Delete a node from the DoublyLinkedList
        dll.delete_node(3)

        # Check that the size of the DoublyLinkedList decreased by 1
        assert len(dll) == 4
