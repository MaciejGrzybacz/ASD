def binary_search(arr, x, left, right):
    """
    Recursive implementation of binary search.
    :param arr: sorted list
    :param x: element to search
    :param left: left index of arr
    :param right: right index of arr
    :return: index of x in arr if present, -1 otherwise
    """
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, x, left, mid - 1)
    else:
        return binary_search(arr, x, mid + 1, right)


def binary_search_iterative(arr, x):
    """
    Iterative implementation of binary search.
    :param arr: sorted list
    :param x: element to search
    :return: index of x in arr if present, -1 otherwise
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def kadane(arr):
    """
    Finds the maximum sum of a subarray in the given array using Kadane's algorithm.
    :param arr: list of integers
    :return: maximum sum of a subarray
    """
    if len(arr) == 0:
        return 0

    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
