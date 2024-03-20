from DataStructures.implementations.stack import Stack

import pytest

class TestStack:

    #  can create an instance of Stack class
    def test_create_instance(self):
        stack = Stack()
        assert isinstance(stack, Stack)

    #  can push data to the stack
    def test_push_data(self):
        stack = Stack()
        stack.push(1)
        assert stack.head.data == 1

    #  can pop data from the stack
    def test_pop_data(self):
        stack = Stack()
        stack.push(1)
        data = stack.pop()
        assert data == 1

    #  can get the size of the stack
    def test_get_size(self):
        stack = Stack()
        assert stack.get_size() == 0
        stack.push(1)
        assert stack.get_size() == 1

    #  can push and pop multiple items to/from the stack
    def test_push_pop_multiple_items(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    #  can push and pop items of different data types to/from the stack
    def test_push_pop_different_data_types(self):
        stack = Stack()
        stack.push(1)
        stack.push("hello")
        stack.push(True)
        assert stack.pop() == True
        assert stack.pop() == "hello"
        assert stack.pop() == 1

    #  can pop from an empty stack and raise an IndexError
    def test_pop_empty_stack(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.pop()

    #  can push and pop to/from a stack with only one item
    def test_push_pop_one_item(self):
        stack = Stack()
        stack.push(1)
        assert stack.pop() == 1

    #  can push and pop to/from a stack with a large number of items
    def test_push_pop_large_number_of_items(self):
        stack = Stack()
        for i in range(1000):
            stack.push(i)
        for i in range(999, -1, -1):
            assert stack.pop() == i

    #  can push and pop to/from a stack with items of large data size
    def test_push_pop_large_data_size(self):
        stack = Stack()
        data = "a" * 1000000
        stack.push(data)
        assert stack.pop() == data

    #  can push and pop items with the same data type to/from the stack
    def test_push_pop_same_data_type(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    #  can push and pop items in a specific order
    def test_push_pop_specific_order(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        stack.push(4)
        assert stack.pop() == 4
        assert stack.pop() == 2
        assert stack.pop() == 1

    #  can push and pop items in a reverse order
    def test_push_and_pop_reverse_order(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    #  can push and pop items in a random order
    def test_push_and_pop_items_random_order(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    #  can push and pop items with special characters and symbols
    def test_push_and_pop_special_characters(self):
        stack = Stack()
        stack.push("!@#$%^&*()")
        stack.push("[]{}<>")
        stack.push("+-*/")
        assert stack.pop() == "+-*/"
        assert stack.pop() == "[]{}<>"
        assert stack.pop() == "!@#$%^&*()"

    #  can push and pop items with leading/trailing whitespaces
    def test_push_and_pop_with_whitespace(self):
        stack = Stack()
        stack.push("   item1   ")
        stack.push("   item2   ")
        assert stack.pop() == "   item2   "
        assert stack.pop() == "   item1   "
