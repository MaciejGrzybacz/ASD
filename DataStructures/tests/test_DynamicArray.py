import pytest

from DataStructures.implementations.dynamicArray import DynamicArray


class TestDynamicArray:

    #  can append data to the array
    def test_append_data(self):
        arr = DynamicArray()
        arr.append(1)
        assert list(arr) == [1]

    #  can remove data from the array
    def test_remove_data(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.remove(1)
        assert list(arr) == [2]

    def test_remove_not_existing_data(self):
        arr = DynamicArray()
        arr.append(1)
        with pytest.raises(ValueError):
            arr.remove(2)

    #  can insert data at a specific index
    def test_insert_data(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(3)
        arr.insert(2, 1)
        assert list(arr) == [1, 2, 3]

    #  can iterate over the array
    def test_iterate_array(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)
        result = []
        for item in arr:
            result.append(item)
        assert result == [1, 2, 3]

    #  can handle appending data when the array is full
    def test_append_full_array(self):
        arr = DynamicArray()
        for i in range(16):
            arr.append(i)
        arr.append(16)
        assert list(arr) == list(range(17))

    #  can handle removing data that doesn't exist in the array
    def test_remove_nonexistent_data(self):
        arr = DynamicArray()
        arr.append(1)
        with pytest.raises(ValueError):
            arr.remove(2)

    #  can handle removing the last element from the array
    def test_remove_last_element(self):
        arr = DynamicArray()
        arr.append(1)
        arr.remove(1)
        assert list(arr) == []

    #  can handle inserting data at index 0
    def test_insert_data_at_index_0(self):
        arr = DynamicArray()
        arr.insert(1, 0)
        assert list(arr) == [1]

    #  can handle inserting data at the last index of the array
    def test_insert_data_at_last_index(self):
        arr = DynamicArray()
        arr.append(1)
        arr.insert(2, 1)
        assert list(arr) == [1, 2]

    #  can handle inserting data at an index beyond the end of the array
    def test_insert_data_beyond_end(self):
        arr = DynamicArray()
        arr.append(1)
        with pytest.raises(IndexError):
            arr.insert(2, 2)

    #  can handle removing data from an array with only one element
    def test_remove_data_single_element(self):
        arr = DynamicArray()
        arr.append(1)
        arr.remove(1)
        assert list(arr) == []

    #  can handle removing data from an array with no elements
    def test_remove_data_no_elements(self):
        arr = DynamicArray()
        with pytest.raises(ValueError):
            arr.remove(1)
