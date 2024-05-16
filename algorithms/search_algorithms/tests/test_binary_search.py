from algorithms.search_algorithms.implementations.binary_search import binary_search, binary_search_iterative
import pytest

def test_binary_search():
    arr = [2, 3, 4, 10, 40]
    assert binary_search(arr, 10, 0, len(arr) - 1) == 3
    assert binary_search(arr, 2, 0, len(arr) - 1) == 0
    assert binary_search(arr, 40, 0, len(arr) - 1) == 4
    assert binary_search(arr, 3, 0, len(arr) - 1) == 1
    assert binary_search(arr, 5, 0, len(arr) - 1) == -1


def test_binary_search_iterative():
    arr = [2, 3, 4, 10, 40]
    assert binary_search_iterative(arr, 10) == 3
    assert binary_search_iterative(arr, 2) == 0
    assert binary_search_iterative(arr, 40) == 4
    assert binary_search_iterative(arr, 3) == 1
    assert binary_search_iterative(arr, 5) == -1


