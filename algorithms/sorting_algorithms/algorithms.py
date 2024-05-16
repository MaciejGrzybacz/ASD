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
