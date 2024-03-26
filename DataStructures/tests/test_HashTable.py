from DataStructures.implementations.hashTable import HashTable

# Dependencies:
import pytest

class TestHashTable:

    #  can insert a key-value pair into the hash table
    def test_insert_key_value_pair(self):
        ht = HashTable()
        ht.insert(1, 10)
        assert ht.get(1) == 10
        assert ht.size == 1
        assert ht.contains_key(1) is True

    #  can get the value of a key from the hash table
    def test_get_value_of_key(self):
        ht = HashTable()
        ht.insert(1, 10)
        assert ht.get(1) == 10

    #  can remove a key-value pair from the hash table
    def test_remove_key_value_pair(self):
        ht = HashTable()
        ht.insert(1, 10)
        ht.remove(1)
        assert ht.contains_key(1) is False
        assert ht.size == 0

    #  can check if a key exists in the hash table
    def test_check_key_exists(self):
        ht = HashTable()
        ht.insert(1, 10)
        assert ht.contains_key(1) is True
        assert ht.contains_key(2) is False

    #  can return a list of all keys in the hash table
    def test_return_all_keys(self):
        ht = HashTable()
        ht.insert(1, 10)
        ht.insert(2, 20)
        assert ht.keys() == [1, 2]

    #  can return a list of all values in the hash table
    def test_return_all_values(self):
        ht = HashTable()
        ht.insert(1, 10)
        ht.insert(2, 20)
        assert ht.values() == [10, 20]

    #  can handle inserting a key-value pair with a key that already exists in the hash table
    def test_handle_existing_key_insertion(self):
        ht = HashTable()
        ht.insert(1, 10)
        with pytest.raises(ValueError):
            ht.insert(1, 20)

    #  can handle removing a key-value pair that doesn't exist in the hash table
    def test_handle_nonexistent_key_removal(self):
        ht = HashTable()
        with pytest.raises(ValueError):
            ht.remove(1)

    #  can handle getting the value of a key that doesn't exist in the hash table
    def test_handle_nonexistent_key_get(self):
        ht = HashTable()
        with pytest.raises(AttributeError):
            ht.get(1)

    #  can handle inserting a large number of key-value pairs into the hash table
    def test_insert_large_number_of_key_value_pairs(self):
        ht = HashTable()
        for i in range(1000):
            ht.insert(i, i * 10)
        assert ht.size == 1000

    #  can handle removing all key-value pairs from the hash table
    def test_remove_all_key_value_pairs(self):
        ht = HashTable()
        for i in range(1000):
            ht.insert(i, i * 10)
        for i in range(1000):
            ht.remove(i)
        assert ht.size == 0


    def test_resize_rehash_and_insert(self):
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
