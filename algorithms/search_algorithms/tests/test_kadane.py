from algorithms.search_algorithms.implementations.kadane_algorithm import kadane

import pytest

class TestKadane:
    def test_max_sum_of_subarray(self):
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        assert kadane(arr) == 6

    def test_all_negative_elements(self):
        arr = [-2, -3, -4, -1, -2, -1, -5, -3]
        assert kadane(arr) == -1

    def test_empty_array(self):
        arr = []
        assert kadane(arr) == 0

    def test_all_elements_zero(self):
        arr = [0, 0, 0, 0]
        assert kadane(arr) == 0

    def test_no_negative_element(self):
        arr = [1, 2, 3, 4, 5]
        assert kadane(arr) == 15
