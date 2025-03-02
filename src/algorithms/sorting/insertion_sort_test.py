from algorithms.insertion_sort import insertion_sort

def test_insertion_sort():
    array = [5, 2, 4, 6, 1, 3]
    expected = [1, 2, 3, 4, 5, 6]
    result = insertion_sort(array)
    assert result == expected