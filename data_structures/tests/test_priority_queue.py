import pytest
from data_structures.implementations.priority_queue import PriorityQueue

def test_create_instance():
    pq = PriorityQueue()
    assert isinstance(pq, PriorityQueue)

def test_push_element():
    pq = PriorityQueue()
    pq.push(5)
    assert pq.heap == [5]

def test_pop_minimum():
    pq = PriorityQueue()
    pq.push(5)
    pq.push(10)
    pq.push(3)
    assert pq.pop() == 3

def test_multiple_elements():
    pq = PriorityQueue()
    pq.push(5)
    pq.push(10)
    pq.push(3)
    assert pq.heap == [3, 10, 5]

def test_repeated_elements():
    pq = PriorityQueue()
    pq.push(5)
    pq.push(5)
    pq.push(5)
    assert pq.heap == [5, 5, 5]

def test_empty_queue():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()

def test_pop_empty_queue():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()

def test_shift_up_negative_index():
    pq = PriorityQueue()
    pq.heap = [5, 10, 3]
    pq.size = 3
    pq.shift_up(-1)
    assert pq.heap == [5, 10, 3]

def test_one_element():
    pq = PriorityQueue()
    pq.push(5)
    assert pq.pop() == 5

def test_handle_identical_elements():
    pq = PriorityQueue()
    pq.push(5)
    pq.push(5)
    pq.push(5)
    assert pq.heap == [5, 5, 5]

def test_pop_elements_order():
    pq = PriorityQueue()
    pq.push(5)
    pq.push(3)
    pq.push(7)
    pq.push(2)
    pq.push(9)
    poped_elements = []
    while pq.size > 0:
        poped_elements.append(pq.pop())
    assert poped_elements == [2, 3, 5, 7, 9]

def test_handle_negative_elements():
    pq = PriorityQueue()
    pq.push(-5)
    pq.push(-10)
    pq.push(-3)
    assert pq.pop() == -10

def test_elements_added_to_correct_positions():
    pq = PriorityQueue()
    pq.push(5)
    assert pq.heap == [5]
    pq.push(10)
    assert pq.heap == [10, 5]
    pq.push(3)
    assert pq.heap == [10, 5, 3]
    pq.push(7)
    assert pq.heap == [10, 7, 3, 5]
    pq.push(2)
    assert pq.heap == [10, 7, 3, 5, 2]
    pq.push(9)
    assert pq.heap == [10, 7, 9, 5, 2, 3]

def test_size_update():
    pq = PriorityQueue()
    assert pq.size == 0
    pq.push(5)
    assert pq.size == 1
    pq.push(10)
    assert pq.size == 2
    pq.push(3)
    assert pq.size == 3
    pq.pop()
    assert pq.size == 2
    pq.pop()
    assert pq.size == 1
    pq.pop()
    assert pq.size == 0

def test_push_negative_elements():
    pq = PriorityQueue()
    pq.push(-5)
    pq.push(-10)
    pq.push(-3)
    assert pq.pop() == -10

def test_elements_added_to_correct_positions():
    pq = PriorityQueue()
    pq.push(5)
    assert pq.heap == [5]
    pq.push(10)
    assert pq.heap == [5, 10]
    pq.push(3)
    assert pq.heap == [3, 10, 5]
    pq.push(7)
    assert pq.heap == [3, 7, 5, 10]
    pq.push(2)
    assert pq.heap == [2, 3, 5, 10, 7]

def test_handle_elements_in_random_order():
    pq = PriorityQueue()
    pq.push(5)
    pq.push(2)
    pq.push(8)
    pq.push(1)
    pq.push(10)
    assert pq.pop() == 1
    assert pq.pop() == 2
    assert pq.pop() == 5
    assert pq.pop() == 8
    assert pq.pop() == 10
