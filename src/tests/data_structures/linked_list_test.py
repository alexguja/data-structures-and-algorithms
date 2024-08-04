import pytest
from data_structures.linked_list import LinkedList, ListNode

def test_is_empty():
    ll = LinkedList()
    assert ll.is_empty() == True
    ll.insert_first(1)
    assert ll.is_empty() == False

def test_insert_first():
    ll = LinkedList()
    ll.insert_first(1)
    assert ll.head.data == 1
    assert ll.tail.data == 1
    assert ll.length == 1
    ll.insert_first(2)
    assert ll.head.data == 2
    assert ll.tail.data == 1
    assert ll.length == 2

def test_insert_last():
    ll = LinkedList()
    ll.insert_last(1)
    assert ll.head.data == 1
    assert ll.tail.data == 1
    assert ll.length == 1
    ll.insert_last(2)
    assert ll.head.data == 1
    assert ll.tail.data == 2
    assert ll.length == 2

def test_build_from():
    ll = LinkedList()
    ll.build_from([1, 2, 3])
    assert ll.head.data == 1
    assert ll.tail.data == 3
    assert ll.length == 3

def test_delete_first():
    ll = LinkedList()
    ll.build_from([1, 2, 3])
    assert ll.delete_first() == 1
    assert ll.head.data == 2
    assert ll.length == 2
    assert ll.delete_first() == 2
    assert ll.head.data == 3
    assert ll.length == 1
    assert ll.delete_first() == 3
    assert ll.head == None
    assert ll.length == 0

def test_delete_last():
    ll = LinkedList()
    ll.build_from([1, 2, 3])
    assert ll.delete_last() == 3
    assert ll.tail.data == 2
    assert ll.length == 2
    assert ll.delete_last() == 2
    assert ll.tail.data == 1
    assert ll.length == 1
    assert ll.delete_last() == 1
    assert ll.tail == None
    assert ll.length == 0

def test_get_at():
    ll = LinkedList()
    ll.build_from([1, 2, 3])
    assert ll.get_at(0) == 1
    assert ll.get_at(1) == 2
    assert ll.get_at(2) == 3
    assert ll.get_at(3) == None

def test_set_at():
    ll = LinkedList()
    ll.build_from([1, 2, 3])
    ll.set_at(1, 4)
    assert ll.get_at(1) == 4
    ll.set_at(0, 5)
    assert ll.get_at(0) == 5
    ll.set_at(2, 6)
    assert ll.get_at(2) == 6

def test_insert_at():
    ll = LinkedList()
    ll.build_from([1, 2, 3])
    ll.insert_at(1, 4)
    assert ll.get_at(1) == 4
    assert ll.get_at(2) == 2
    ll.insert_at(0, 5)
    assert ll.get_at(0) == 5
    assert ll.get_at(1) == 1
    ll.insert_at(5, 6)
    assert ll.get_at(5) == 6

def test_delete_at():
    ll = LinkedList()
    ll.build_from([1, 2, 3])
    assert ll.delete_at(1) == 2
    assert ll.get_at(1) == 3
    assert ll.length == 2
    assert ll.delete_at(0) == 1
    assert ll.get_at(0) == 3
    assert ll.length == 1
    assert ll.delete_at(0) == 3
    assert ll.length == 0

def test_str():
    ll = LinkedList()
    assert str(ll) == ""
    ll.build_from([1, 2, 3])
    assert str(ll) == "Head -> 1 -> 2 -> 3 -> None"

if __name__ == "__main__":
    pytest.main()