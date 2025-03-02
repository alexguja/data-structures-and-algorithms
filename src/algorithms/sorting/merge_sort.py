def merge_sort(array: list, start: int, end: int):
    """Sorts an array using the merge sort algorithm.

    Args:
        array (List[int]): Elements to be sorted.

    Returns:
        List[int]: Sorted elements.
    """

    # Time Complexity: O(n lg n) -> O(n) for merge and O(lg n) for the recursion
    # Space Complexity: O(n)

    if start < end:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        merge(array, start, mid, end) # Time Complexity: O(n)


def merge(array: list, start: int, mid: int,end:int):
    """Merges two sorted arrays into a single sorted array.

    Args:
        left (List[int]): Left array.
        right (List[int]): Right array.

    Returns:
        List[int]: Merged array.
    """
    n1 = mid - start + 1
    n2 = end - mid

    # Create two temporary arrays
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)

    for i in range(n1):
        left[i] = array[start + i]
    for j in range(n2):
        right[j] = array[mid + 1 + j]

    left[n1] = float('inf')
    right[n2] = float('inf')

    i = j = 0

    for k in range(start, end + 1):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

