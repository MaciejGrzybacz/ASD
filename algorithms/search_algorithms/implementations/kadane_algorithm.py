def kadane(arr):
    """
    Finds the maximum sum of a subarray in the given array using Kadane's algorithm.

    Args:
    - arr: A list of integers representing the input array.

    Returns:
    - max_sum: The maximum sum of a subarray in the input array.
    """
    if len(arr) == 0:
        return 0
    
    max_sum = arr[0]
    current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
