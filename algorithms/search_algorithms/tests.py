from algorithms.search_algorithms.algorithms import binary_search, binary_search_iterative, kadane


def test_recursive_binary_search():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(arr, 5, 0, len(arr) - 1) == 4
    assert binary_search(arr, 10, 0, len(arr) - 1) == 9
    assert binary_search(arr, 1, 0, len(arr) - 1) == 0
    assert binary_search(arr, 0, 0, len(arr) - 1) == -1
    assert binary_search(arr, 11, 0, len(arr) - 1) == -1


def test_iterative_binary_search():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search_iterative(arr, 5) == 4
    assert binary_search_iterative(arr, 10) == 9
    assert binary_search_iterative(arr, 1) == 0
    assert binary_search_iterative(arr, 0) == -1
    assert binary_search_iterative(arr, 11) == -1


def test_kadane():
    assert kadane([1, 2, 3, 4, 5]) == 15
    assert kadane([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
    assert kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert kadane([1]) == 1
    assert kadane([-1]) == -1
    assert kadane([]) == 0
    assert kadane([1, 2, 3, -2, 5]) == 9
    assert kadane([1, 2, 3, -2, 5, -1, 2, 3, -2, 5]) == 16
    assert kadane([1, 2, 3, -2, 5, -1, 2, 3, -2, 5, -1, 2, 3, -2, 5]) == 23
    assert kadane([-1, -2, -3, -4, -5]) == -1
