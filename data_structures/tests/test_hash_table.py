import pytest
from data_structures.implementations.hash_table import HashTable

def test_insert_key_value_pair():
    ht = HashTable()
    ht.insert(1, 10)
    assert ht.get(1) == 10
    assert ht.size == 1
    assert ht.contains_key(1) is True

def test_get_value_of_key():
    ht = HashTable()
    ht.insert(1, 10)
    assert ht.get(1) == 10

def test_remove_key_value_pair():
    ht = HashTable()
    ht.insert(1, 10)
    ht.remove(1)
    assert ht.contains_key(1) is False
    assert ht.size == 0

def test_check_key_exists():
    ht = HashTable()
    ht.insert(1, 10)
    assert ht.contains_key(1) is True
    assert ht.contains_key(2) is False

def test_return_all_keys():
    ht = HashTable()
    ht.insert(1, 10)
    ht.insert(2, 20)
    assert ht.keys() == [1, 2]

def test_return_all_values():
    ht = HashTable()
    ht.insert(1, 10)
    ht.insert(2, 20)
    assert ht.values() == [10, 20]

def test_handle_existing_key_insertion():
    ht = HashTable()
    ht.insert(1, 10)
    with pytest.raises(ValueError):
        ht.insert(1, 20)

def test_handle_nonexistent_key_removal():
    ht = HashTable()
    with pytest.raises(ValueError):
        ht.remove(1)

def test_handle_nonexistent_key_get():
    ht = HashTable()
    with pytest.raises(AttributeError):
        ht.get(1)

def test_insert_large_number_of_key_value_pairs():
    ht = HashTable()
    for i in range(1000):
        ht.insert(i, i * 10)
    assert ht.size == 1000

def test_remove_all_key_value_pairs():
    ht = HashTable()
    for i in range(1000):
        ht.insert(i, i * 10)
    for i in range(1000):
        ht.remove(i)
    assert ht.size == 0

def test_resize_rehash_and_insert():
    hash_table = HashTable()
    hash_table.insert(1, 10)
    hash_table.insert(2, 20)
    hash_table.insert(3, 30)
    old_table = hash_table.table
    hash_table.resize()
    new_table = hash_table.table
    for i in range(len(old_table)):
        curr = old_table[i]
        while curr:
            assert new_table[hash_table.hash(curr.key)] == curr
            curr = curr.next
