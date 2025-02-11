"""Closed-box unit tests for all Stack ADT implementations."""

from collections.abc import Sequence

import pytest

from paddles.stack import DynamicArrayStack, LinkedListStack

# Helper functions: can't be named test_... or pytest will call them directly.

StackADT = DynamicArrayStack | LinkedListStack


def check_is_empty(stack: StackADT) -> None:
    """Test that the stack is empty."""
    assert stack.size() == 0
    with pytest.raises(ValueError, match="can't peek into an empty stack"):
        stack.peek()
    with pytest.raises(ValueError, match="can't pop a member from an empty stack"):
        stack.pop()
    assert str(stack) == f"{stack.__class__.__name__}([])"


# Execute each test for all combinations of these parameter values.
pytestmark = [
    pytest.mark.parametrize("Stack", [LinkedListStack, DynamicArrayStack]),
    pytest.mark.parametrize(
        "sequence", ["abcd", [3, 2, 1], (True, False, None), range(20)]
    ),
]

# Test the creation methods.


def test_init_empty(Stack: type[StackADT], sequence: Sequence) -> None:  # noqa: N803 ARG001
    """Test the creation of empty stacks.

    Ignore `sequence` as it's not needed for this one test.
    """
    check_is_empty(Stack())


def test_init_iterable(Stack: type[StackADT], sequence: Sequence) -> None:  # noqa: N803
    """Test the creation of stacks from sequences."""
    stack = Stack(sequence)
    assert stack.size() == len(sequence)
    assert stack.peek() == sequence[-1]
    assert str(stack) == f"{Stack.__name__}({list(sequence)})"


# Test each modifier method separately.


def test_push(Stack: type[StackADT], sequence: Sequence) -> None:  # noqa: N803
    """Test that `push(item)` adds `item` to the top."""
    stack = Stack()
    for item in sequence:
        before = stack.size()
        stack.push(item)
        assert stack.size() == before + 1
        assert stack.peek() == item
    assert str(stack) == f"{Stack.__name__}({list(sequence)})"


def test_pop(Stack: type[StackADT], sequence: Sequence) -> None:  # noqa: N803
    """Test that `pop()` removes and returns the top item."""
    stack = Stack(sequence)
    for _ in sequence:
        before = stack.size()
        assert stack.peek() == stack.pop()
        assert stack.size() == before - 1
    check_is_empty(stack)


# Test the combined behaviour of modifiers.


def test_lifo(Stack: type[StackADT], sequence: Sequence) -> None:  # noqa: N803
    """Test the last-in first-out behaviour of stacks."""
    stack = Stack()
    for item in sequence:
        stack.push(item)
    for item in reversed(sequence):
        assert stack.pop() == item
    check_is_empty(stack)
