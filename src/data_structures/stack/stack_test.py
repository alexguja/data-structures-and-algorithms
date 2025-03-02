import pytest
from data_structures.stack.stack import Stack


def test_stack():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.is_empty() == False
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.pop() == 1
    assert stack.is_empty() == True
    try:
        stack.pop()
    except ValueError as e:
        assert str(e) == "Stack underflow"
    try:
        stack.peek()
    except ValueError as e:
        assert str(e) == "Stack underflow"
    print("Stack tests pass")
