
from DataStructures.implementations.queue import Queue

import pytest

class TestQueue:

    #  Enqueueing a single element should increase the size of the queue by 1
    def test_enqueue_single_element(self):
        queue = Queue()
        queue.enqueue(1)
        assert queue.size == 1

    #  Enqueueing multiple elements should increase the size of the queue by the number of elements
    def test_enqueue_multiple_elements(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.size == 3

    #  Dequeueing an element from a non-empty queue should decrease the size of the queue by 1
    def test_dequeue_non_empty_queue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        assert queue.size == 1

    #  Enqueueing and dequeueing elements in alternating order should maintain the correct size of the queue
    def test_enqueue_dequeue_alternating_order_size(self):
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()
        queue.enqueue(2)
        queue.dequeue()
        assert queue.size == 0

    #  Enqueueing and dequeueing elements in alternating order should maintain the correct order of the elements
    def test_enqueue_dequeue_alternating_order_order(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2

    #  Enqueueing and dequeueing elements in alternating order should maintain the correct head and tail of the queue
    def test_enqueue_dequeue_alternating_order_head_tail(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.head.data == 1
        assert queue.tail.data == 2

    #  Dequeueing an element from an empty queue should raise a ValueError
    def test_dequeue_empty_queue(self):
        queue = Queue()
        with pytest.raises(ValueError):
            queue.dequeue()

    #  Enqueueing None should add None to the queue
    def test_enqueue_none(self):
        queue = Queue()
        queue.enqueue(None)
        assert queue.size == 1
        assert queue.head.data is None
        assert queue.tail.data is None

    #  Enqueueing and dequeueing elements until the queue is empty should maintain the correct size of the queue
    def test_enqueue_dequeue_until_empty_size(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        queue.dequeue()
        assert queue.size == 0

    #  Enqueueing and dequeueing elements until the queue is empty should maintain the correct order of the elements
    def test_enqueue_dequeue_until_empty_order(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2

    #  Enqueueing and dequeueing elements until the queue is empty should maintain the correct head and tail of the queue
    def test_enqueue_dequeue_until_empty_head_tail(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.head.data == 1
        assert queue.tail.data == 2

    #  Dequeueing elements beyond the current size of the queue should raise an exception
    def test_dequeue_beyond_size(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        with pytest.raises(ValueError):
            queue.dequeue()
            queue.dequeue()
            queue.dequeue()
            queue.dequeue()

    #  Enqueueing elements with different data types should maintain the correct order of the elements
    def test_enqueue_different_data_types(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue("two")
        queue.enqueue(3.0)
        assert queue.dequeue() == 1
        assert queue.dequeue() == "two"
        assert queue.dequeue() == 3.0

    #  Enqueueing and dequeueing elements with different data types should maintain the correct size of the queue
    def test_enqueue_dequeue_different_data_types(self):
        # Create an instance of the Queue class
        queue = Queue()

        # Enqueue elements of different data types
        queue.enqueue(1)
        queue.enqueue("hello")
        queue.enqueue([1, 2, 3])
        queue.enqueue({"name": "John", "age": 30})

        # Assert that the size of the queue is correct after enqueueing
        assert queue.size == 4

        # Dequeue elements and assert that the size of the queue is correct after each dequeue
        assert queue.dequeue() == 1
        assert queue.size == 3

        assert queue.dequeue() == "hello"
        assert queue.size == 2

        assert queue.dequeue() == [1, 2, 3]
        assert queue.size == 1

        assert queue.dequeue() == {"name": "John", "age": 30}
        assert queue.size == 0

    #  Enqueueing and dequeueing elements with different data types should maintain the correct head and tail of the queue
    def test_enqueue_dequeue_different_data_types(self):
        queue = Queue()
        # Enqueue elements with different data types
        queue.enqueue(1)
        queue.enqueue("two")
        queue.enqueue(3.0)
        queue.enqueue([4, 5, 6])
    
        # Dequeue elements and check if head and tail are maintained correctly
        assert queue.dequeue() == 1
        assert queue.head.data == "two"
        assert queue.tail.data == [4, 5, 6]
    
        assert queue.dequeue() == "two"
        assert queue.head.data == 3.0
        assert queue.tail.data == [4, 5, 6]
    
        assert queue.dequeue() == 3.0
        assert queue.head.data == [4, 5, 6]
        assert queue.tail.data == [4, 5, 6]
    
        assert queue.dequeue() == [4, 5, 6]
        assert queue.head is None
        assert queue.tail is None
