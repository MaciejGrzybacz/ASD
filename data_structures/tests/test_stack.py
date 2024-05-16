import pytest
from data_structures.implementations.stack import Stack

def test_create_instance():
    stack = Stack()
    assert isinstance(stack, Stack)

def test_push_data():
    stack = Stack()
    stack.push(1)
    assert stack.head.data == 1

def test_pop_data():
    stack = Stack()
    stack.push(1)
    data = stack.pop()
    assert data == 1

def test_get_size():
    stack = Stack()
    assert stack.get_size() == 0
    stack.push(1)
    assert stack.get_size() == 1

def test_push_pop_multiple_items():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_pop_empty_stack():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()

def test_push_pop_one_item():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1

def test_push_pop_large_number_of_items():
    stack = Stack()
    for i in range(1000):
        stack.push(i)
    for i in range(999, -1, -1):
        assert stack.pop() == i


def test_push_pop_specific_order():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    stack.push(4)
    assert stack.pop() == 4
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_push_and_pop_reverse_order():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_push_and_pop_items_random_order():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
