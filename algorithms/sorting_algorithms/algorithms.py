"""
This module contains the implementation of the following sorting algorithms:
- Bubble Sort
- Insertion Sort
- Selection Sort
- Bucket Sort
- Count Sort
- Quick Sort
- Merge Sort

Each function takes a list and returns a sorted list. The functions are tested in algorithms/sorting_algorithms/tests.py.

"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        num = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > num:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = num
    return arr


def select_sort(arr):
    n = len(arr)
    for i in range(n):
        next_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[next_min]:
                next_min = j
        arr[i], arr[next_min] = arr[next_min], arr[i]
    return arr


def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return arr
    arr_min = min(arr)
    arr_max = max(arr)
    bucket_size = (arr_max - arr_min) / n
    bucket = [[] for _ in range(n)]
    for i in range(n):
        bucket_index = int((arr[i] - arr_min) / bucket_size)
        if bucket_index == n:
            bucket_index -= 1
        bucket[bucket_index].append(arr[i])
    for i in range(n):
        bucket[i].sort()
    index = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            arr[index] = bucket[i][j]
            index += 1
    return arr


def count_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    for i in range(len(arr)):
        count_arr[arr[i] - min_val] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]

    return arr


def partition(arr, left, right):
    x = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr, left=None, right=None):
    if left is None:
        left, right = 0, len(arr) - 1
    while left < right:
        q = partition(arr, left, right)
        if q - left < right - q:
            quick_sort(arr, left, q - 1)
            left = q + 1
        else:
            quick_sort(arr, q + 1, right)
            right = q - 1
    return arr


def merge(left_arr, right_arr):
    merged = [0] * (len(left_arr) + len(right_arr))
    i, j = 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merged[i + j] = left_arr[i]
            i += 1
        else:
            merged[i + j] = right_arr[j]
            j += 1

    while i < len(left_arr):
        merged[i + j] = left_arr[i]
        i += 1

    while j < len(right_arr):
        merged[i + j] = right_arr[j]
        j += 1

    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr, right_arr)
