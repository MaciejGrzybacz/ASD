import pytest
from .algorithms import bubble_sort, insert_sort, select_sort, bucket_sort, count_sort, quick_sort, merge_sort


def test_bubble_sort():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([3, 2, 1, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([3, 2, 1, 4, 5, 0]) == [0, 1, 2, 3, 4, 5]


def test_insert_sort():
    assert insert_sort([3, 2, 1]) == [1, 2, 3]
    assert insert_sort([3, 2, 1, 4, 5]) == [1, 2, 3, 4, 5]
    assert insert_sort([3, 2, 1, 4, 5, 0]) == [0, 1, 2, 3, 4, 5]


def test_select_sort():
    assert select_sort([3, 2, 1]) == [1, 2, 3]
    assert select_sort([3, 2, 1, 4, 5]) == [1, 2, 3, 4, 5]
    assert select_sort([3, 2, 1, 4, 5, 0]) == [0, 1, 2, 3, 4, 5]


def test_bucket_sort():
    assert bucket_sort([3, 2, 1]) == [1, 2, 3]
    assert bucket_sort([3, 2, 1, 4, 5]) == [1, 2, 3, 4, 5]
    assert bucket_sort([3, 2, 1, 4, 5, 0]) == [0, 1, 2, 3, 4, 5]


def test_count_sort():
    assert count_sort([3, 2, 1]) == [1, 2, 3]
    assert count_sort([3, 2, 1, 4, 5]) == [1, 2, 3, 4, 5]
    assert count_sort([3, 2, 1, 4, 5, 0]) == [0, 1, 2, 3, 4, 5]


def test_quick_sort():
    assert quick_sort([3, 2, 1]) == [1, 2, 3]
    assert quick_sort([3, 2, 1, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick_sort([3, 2, 1, 4, 5, 0]) == [0, 1, 2, 3, 4, 5]


def test_merge_sort():
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([3, 2, 1, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([3, 2, 1, 4, 5, 0]) == [0, 1, 2, 3, 4, 5]
