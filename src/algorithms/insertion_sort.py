from typing import List

def insertion_sort(array):
    """Sorts an array in place using insertion sort in O(n^2) time.

    Args:
        array (List): The array to be sorted.

    Returns:
        List: The sorted array.
    
    Example:
        Given an array [5, 2, 4, 6, 1, 3]. 
        
        The algorithm will sort the array as follows:

        Step 1: Swaps 5 and 2
            [5, 2, 4, 6, 1, 3] => [2, 5, 4, 6, 1, 3]
        
        Step 2: Swaps 5 and 4
            [2, 5, 4, 6, 1, 3] => [2, 4, 5, 6, 1, 3]
        
        Step 3: No swaps
            [2, 4, 5, 6, 1, 3] => [2, 4, 5, 6, 1, 3]
        
        Step 4: Move 1 to the front and shift the rest
            [2, 4, 5, 6, 1, 3] => [1, 2, 4, 5, 6, 3]
        
        Step 5: Move 3 to the correct position and shift the rest
            [1, 2, 4, 5, 6, 3] => [1, 2, 3, 4, 5, 6]

    """
    for i in range(1, len(array)):
        key = array[i] 
        j = i -1 
        while j >= 0 and array[j] > key: 
            array[j + 1] = array[j] 
            j -= 1
        array[j + 1] = key 

    return array

        