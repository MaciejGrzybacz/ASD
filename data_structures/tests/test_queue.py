import pytest
from data_structures.implementations.queue import Queue

def test_enqueue_single_element():
    queue = Queue()
    queue.enqueue(1)
    assert queue.size == 1

def test_enqueue_multiple_elements():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.size == 3

def test_dequeue_non_empty_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    assert queue.size == 1

def test_enqueue_dequeue_alternating_order_size():
    queue = Queue()
    queue.enqueue(1)
    queue.dequeue()
    queue.enqueue(2)
    queue.dequeue()
    assert queue.size == 0

def test_enqueue_dequeue_alternating_order_order():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

def test_enqueue_dequeue_alternating_order_head_tail():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.head.data == 1
    assert queue.tail.data == 2

def test_dequeue_empty_queue():
    queue = Queue()
    with pytest.raises(ValueError):
        queue.dequeue()

def test_enqueue_none():
    queue = Queue()
    queue.enqueue(None)
    assert queue.size == 1
    assert queue.head.data is None
    assert queue.tail.data is None

def test_enqueue_dequeue_until_empty_size():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    assert queue.size == 0

def test_enqueue_dequeue_until_empty_order():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

def test_enqueue_dequeue_until_empty_head_tail():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.head.data == 1
    assert queue.tail.data == 2

def test_dequeue_beyond_size():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    with pytest.raises(ValueError):
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()

def test_enqueue_different_data_types():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue("two")
    queue.enqueue(3.0)
    assert queue.dequeue() == 1
    assert queue.dequeue() == "two"
    assert queue.dequeue() == 3.0

def test_enqueue_dequeue_different_data_types():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue("hello")
    queue.enqueue([1, 2, 3])
    queue.enqueue({"name": "John", "age": 30})
    assert queue.size == 4
    assert queue.dequeue() == 1
    assert queue.size == 3
    assert queue.dequeue() == "hello"
    assert queue.size == 2
    assert queue.dequeue() == [1, 2, 3]
    assert queue.size == 1
    assert queue.dequeue() == {"name": "John", "age": 30}
    assert queue.size == 0

