from DataStructures.implementations.priorityQueue import PriorityQueue

import pytest


class TestPriorityQueue:

    #  can create an instance of PriorityQueue
    def test_create_instance(self):
        pq = PriorityQueue()
        assert isinstance(pq, PriorityQueue)

    #  can push an element to the queue
    def test_push_element(self):
        pq = PriorityQueue()
        pq.push(5)
        assert pq.heap == [5]

    #  can pop the minimum element from the queue
    def test_pop_minimum(self):
        pq = PriorityQueue()
        pq.push(5)
        pq.push(10)
        pq.push(3)
        assert pq.pop() == 3

    #  can handle multiple elements in the queue
    def test_multiple_elements(self):
        pq = PriorityQueue()
        pq.push(5)
        pq.push(10)
        pq.push(3)
        assert pq.heap == [3, 10, 5]

    #  can handle repeated elements in the queue
    def test_repeated_elements(self):
        pq = PriorityQueue()
        pq.push(5)
        pq.push(5)
        pq.push(5)
        assert pq.heap == [5, 5, 5]

    #  can handle empty queue popion
    def test_empty_queue(self):
        pq = PriorityQueue()
        with pytest.raises(IndexError):
            pq.pop()

    #  can handle popping from an empty queue
    def test_pop_empty_queue(self):
        pq = PriorityQueue()
        with pytest.raises(IndexError):
            pq.pop()

    #  can handle shifting up with a negative index
    def test_shift_up_negative_index(self):
        pq = PriorityQueue()
        pq.heap = [5, 10, 3]
        pq.size = 3
        pq.shift_up(-1)
        assert pq.heap == [5, 10, 3]

    #  can handle one element in the queue
    def test_one_element(self):
        pq = PriorityQueue()
        pq.push(5)
        assert pq.pop() == 5

    #  can handle identical elements in the queue
    def test_handle_identical_elements(self):
        pq = PriorityQueue()
        pq.push(5)
        pq.push(5)
        pq.push(5)
        assert pq.heap == [5, 5, 5]

    #  Extract the elements from the queue and verify that they are in the correct order.
    def test_pop_elements_order(self):
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

    #  can handle negative elements in the queue
    def test_handle_negative_elements(self):
        pq = PriorityQueue()
        pq.push(-5)
        pq.push(-10)
        pq.push(-3)
        assert pq.pop() == -10

    #  Verify that the elements are added to the correct positions in the heap.
    def test_elements_added_to_correct_positions(self):
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

    #  Verify that the size of the queue is updated correctly after each operation.
    def test_size_update(self):
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

    #  Push negative elements to the queue.
    def test_push_negative_elements(self):
        pq = PriorityQueue()
        pq.push(-5)
        pq.push(-10)
        pq.push(-3)
        assert pq.pop() == -10

    #  Verify that the elements are added to the correct positions in the heap.
    def test_elements_added_to_correct_positions(self):
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

    #  can handle float elements in the queue
    def test_handle_float_elements(self):
        pq = PriorityQueue()
        pq.push(5.5)
        pq.push(10.2)
        pq.push(3.7)
        assert pq.pop() == 3.7

    #  can handle large input sizes
    def test_handle_large_input_sizes(self):
        pq = PriorityQueue()
        input_size = 1000
        for i in range(input_size):
            pq.push(i)
        for i in range(0, input_size):
            assert pq.pop() == i


    #  can handle elements in random order
    def test_handle_elements_in_random_order(self):
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
