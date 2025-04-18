def binary_search(array, target):
    """Performs a binary search on a sorted array.

    Args:
        array (List[int]): The sorted list of integers in which to search.
        target (int): The value to search for in the array.

    Returns:
        int: The index of the target in the array if found, otherwise -1.
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if target < array[mid]:
            high = mid - 1
        elif target > array[mid]:
            low = mid + 1
        else:
            return mid
    return -1
