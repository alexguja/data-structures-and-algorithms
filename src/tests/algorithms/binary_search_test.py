import pytest
from algorithms.binary_search import binary_search, optimised_binary_search

def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([], 3) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([1, 2, 2, 2, 3], 2) == 2

def test_optimised_binary_search():
    assert optimised_binary_search([1, 2, 3, 4, 5], 3) == 2
    assert optimised_binary_search([1, 2, 3, 4, 5], 6) == -1
    assert optimised_binary_search([], 3) == -1
    assert optimised_binary_search([1], 1) == 0
    assert optimised_binary_search([1, 2, 2, 2, 3], 2) == 2

if __name__ == "__main__":
    pytest.main()