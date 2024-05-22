import pytest
from data_structures.linked_lists.doubly_linked_list.doubly_linked_list import DoublyLinkedList

def test_empty_list_size():
    dll = DoublyLinkedList()
    assert len(dll) == 0

def test_append_element():
    dll = DoublyLinkedList()
    dll.append(1)
    assert len(dll) == 1

def test_prepend_element():
    dll = DoublyLinkedList()
    dll.prepend(1)
    assert len(dll) == 1

def test_insert_after_node():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.insert_after_node(dll.head, 2)
    assert len(dll) == 2

def test_delete_node():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.delete_node(1)
    assert dll.head == None
    assert dll.tail == None
    assert len(dll) == 0

def test_delete_first_node():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.delete_node(1)
    assert len(dll) == 1

def test_delete_node_empty_list():
    dll = DoublyLinkedList()
    with pytest.raises(ValueError):
        dll.delete_node(1)

def test_insert_after_none_node():
    dll = DoublyLinkedList()
    with pytest.raises(ValueError):
        dll.insert_after_node(None, 1)

def test_delete_node_key_not_found():
    dll = DoublyLinkedList()
    dll.append(1)
    with pytest.raises(ValueError):
        dll.delete_node(2)

def test_delete_node_invalid_position():
    dll = DoublyLinkedList()
    dll.append(1)
    with pytest.raises(ValueError):
        dll.delete_node_at_position(1)

def test_delete_node_position_0_size_1():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.delete_node_at_position(0)
    assert len(dll) == 0

def test_delete_node_last_position_size_1():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.delete_node_at_position(0)
    assert len(dll) == 0

def test_delete_last_node_size_decreased():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.delete_node(3)
    assert len(dll) == 2

def test_reverse_doubly_linked_list():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.reverse()
    assert list(dll) == [5, 4, 3, 2, 1]

def test_insert_after_first_node_size_increased():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.insert_after_node(dll.head, 4)
    assert len(dll) == 4

def test_create_doubly_linked_list_with_multiple_elements():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert len(dll) == 3

def test_insert_after_middle_node_size_increased():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.insert_after_node(dll.head.next, 5)
    assert len(dll) == 5

def test_insert_after_last_node():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    initial_size = len(dll)
    dll.insert_after_node(dll.tail, 4)
    assert len(dll) == initial_size + 1

def test_delete_node_size_decrease():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.delete_node(3)
    assert len(dll) == 4
