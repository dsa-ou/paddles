"""Closed-box unit tests for all Stack ADT implementations."""

import pytest

from paddles.stack import DynamicArrayStack, LinkedListStack

# Helper functions: can't be named test_... or pytest will call them directly.


def check_is_empty(stack):
    """Test that the stack is empty."""
    assert stack.size() == 0
    with pytest.raises(ValueError):
        stack.peek()
    with pytest.raises(ValueError):
        stack.pop()
    assert str(stack) == f"{stack.__class__.__name__}([])"


# Fixtures: functions that return the data for testing the stack operations.


@pytest.fixture(params=[DynamicArrayStack, LinkedListStack])
def Stack(request):
    """Return an implementation (a class) to be tested."""
    return request.param


@pytest.fixture(params=["abcd", [1, 2, 3], (True, False, None), range(20)])
def sequence(request):
    """Return a sequence of items to test with."""
    return request.param


# Test the creation methods.


def test_init_empty(Stack):
    """Test the creation of empty stacks."""
    check_is_empty(Stack())


def test_init_iterable(Stack, sequence):
    """Test the creation of stacks from sequences."""
    stack = Stack(sequence)
    assert stack.size() == len(sequence)
    assert stack.peek() == sequence[-1]
    assert str(stack) == f"{Stack.__name__}({list(sequence)})"


# Test each modifier method separately.


def test_push(Stack, sequence):
    """Test that `push(item)` adds `item` to the top."""
    stack = Stack()
    for item in sequence:
        before = stack.size()
        stack.push(item)
        assert stack.size() == before + 1
        assert stack.peek() == item
    assert str(stack) == f"{Stack.__name__}({list(sequence)})"


def test_pop(Stack, sequence):
    """Test that `pop()` removes and returns the top item."""
    stack = Stack(sequence)
    for _ in sequence:
        before = stack.size()
        assert stack.peek() == stack.pop()
        assert stack.size() == before - 1
    check_is_empty(stack)


# Test the combined behaviour of modifiers.


def test_lifo(Stack, sequence):
    """Test the last-in first-out behaviour of stacks."""
    stack = Stack()
    for item in sequence:
        stack.push(item)
    for item in reversed(sequence):
        assert stack.pop() == item
    check_is_empty(stack)
