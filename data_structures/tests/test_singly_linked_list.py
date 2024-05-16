import pytest
from data_structures.implementations.singly_linked_list import SinglyLinkedList

def test_empty_list_size():
    lst = SinglyLinkedList()
    assert len(lst) == 0

def test_append_to_empty_list():
    lst = SinglyLinkedList()
    lst.append(1)
    assert len(lst) == 1
    assert lst.head.data == 1

def test_append_to_non_empty_list():
    lst = SinglyLinkedList()
    lst.append(1)
    lst.append(2)
    assert len(lst) == 2
    assert lst.tail.data == 2

def test_insert_at_index_0():
    lst = SinglyLinkedList()
    lst.insert(1, 0)
    assert len(lst) == 1
    assert lst.head.data == 1

def test_insert_at_end():
    lst = SinglyLinkedList()
    lst.append(1)
    lst.insert(2, 1)
    assert len(lst) == 2
    assert lst.tail.data == 2

def test_insert_at_valid_index():
    lst = SinglyLinkedList()
    lst.append(1)
    lst.append(3)
    lst.insert(2, 1)
    assert len(lst) == 3
    assert lst.head.next.data == 2

def test_insert_at_invalid_negative_index():
    lst = SinglyLinkedList()
    with pytest.raises(IndexError):
        lst.insert(1, -1)

def test_insert_at_invalid_positive_index():
    lst = SinglyLinkedList()
    with pytest.raises(IndexError):
        lst.insert(1, 1)

def test_remove_from_empty_list():
    lst = SinglyLinkedList()
    with pytest.raises(ValueError):
        lst.remove(1)

def test_remove_non_existent_element():
    lst = SinglyLinkedList()
    lst.append(1)
    with pytest.raises(ValueError):
        lst.remove(2)

def test_remove_only_element_and_try_remove_another():
    lst = SinglyLinkedList()
    lst.append(1)
    lst.remove(1)
    with pytest.raises(ValueError):
        lst.remove(2)

def test_remove_head_element():
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.remove(1)
    assert len(linked_list) == 2
    assert linked_list.head.data == 2

def test_remove_non_head_element():
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.remove(3)
    assert len(linked_list) == 3
    assert linked_list.to_list() == [1, 2, 4]

def test_remove_only_element():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.remove(10)
    assert len(linked_list) == 0
    assert linked_list.head is None

def test_reverse_non_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.reverse()
    assert linked_list.head.data == 4
    assert linked_list.tail.data == 1

def test_iterating_through_list():
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    result = []
    for element in linked_list:
        result.append(element)
    assert result == [1, 2, 3]

def test_clear_method():
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.clear()
    assert len(linked_list) == 0
    assert linked_list.head is None

def test_converting_to_list():
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    result = linked_list.to_list()
    assert result == [1, 2, 3]

def test_insert_at_index_0_non_empty_list():
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.insert(0, 0)
    assert linked_list.head.data == 0
    assert linked_list.head.next.data == 1

def test_insert_at_end_with_one_element():
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.insert(2, 1)
    assert linked_list.head.next.data == 2
