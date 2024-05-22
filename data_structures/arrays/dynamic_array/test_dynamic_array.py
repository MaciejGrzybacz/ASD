import pytest
from data_structures.arrays.dynamic_array.dynamic_array import DynamicArray

def test_append_data():
    arr = DynamicArray()
    arr.append(1)
    assert list(arr) == [1]

def test_remove_data():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.remove(1)
    assert list(arr) == [2]

def test_remove_not_existing_data():
    arr = DynamicArray()
    arr.append(1)
    with pytest.raises(ValueError):
        arr.remove(2)

def test_insert_data():
    arr = DynamicArray()
    arr.append(1)
    arr.append(3)
    arr.insert(2, 1)
    assert list(arr) == [1, 2, 3]

def test_iterate_array():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    result = []
    for item in arr:
        result.append(item)
    assert result == [1, 2, 3]

def test_append_full_array():
    arr = DynamicArray()
    for i in range(16):
        arr.append(i)
    arr.append(16)
    assert list(arr) == list(range(17))

def test_remove_nonexistent_data():
    arr = DynamicArray()
    arr.append(1)
    with pytest.raises(ValueError):
        arr.remove(2)

def test_remove_last_element():
    arr = DynamicArray()
    arr.append(1)
    arr.remove(1)
    assert list(arr) == []

def test_insert_data_at_index_0():
    arr = DynamicArray()
    arr.insert(1, 0)
    assert list(arr) == [1]

def test_insert_data_at_last_index():
    arr = DynamicArray()
    arr.append(1)
    arr.insert(2, 1)
    assert list(arr) == [1, 2]

def test_insert_data_beyond_end():
    arr = DynamicArray()
    arr.append(1)
    with pytest.raises(IndexError):
        arr.insert(2, 2)

def test_remove_data_single_element():
    arr = DynamicArray()
    arr.append(1)
    arr.remove(1)
    assert list(arr) == []

def test_remove_data_no_elements():
    arr = DynamicArray()
    with pytest.raises(ValueError):
        arr.remove(1)
