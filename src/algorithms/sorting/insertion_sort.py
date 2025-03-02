from typing import List


def insertion_sort(array):
    """Sorts an array in place using insertion sort in O(n^2) time."""
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array
