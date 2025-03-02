import pytest
from data_structures.heap.heap import MaxHeap


def test_max_heap_insert_and_extract():
    heap = MaxHeap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(2)

    assert heap.extract_max() == 3
    assert heap.extract_max() == 2
    assert heap.extract_max() == 1


def test_max_heap_empty_extract_max():
    heap = MaxHeap()
    with pytest.raises(IndexError):
        heap.extract_max()
