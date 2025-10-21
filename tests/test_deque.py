"""Closed-box unit tests for all implementations of the Deque ADT."""

from collections.abc import Sequence

import pytest

from paddles import LinkedListDeque

# Helper functions: can't be named test_... or pytest will call them directly.

DequeADT = LinkedListDeque


def check_is_empty(deque: DequeADT) -> None:
    """Test that the deque is empty."""
    assert deque.size() == 0
    with pytest.raises(ValueError, match="can't access the front of an empty deque"):
        deque.front()
    with pytest.raises(ValueError, match="can't access the back of an empty deque"):
        deque.back()
    with pytest.raises(ValueError, match="can't remove a member from an empty deque"):
        deque.take_front()
    with pytest.raises(ValueError, match="can't remove a member from an empty deque"):
        deque.take_back()
    assert str(deque) == f"{deque.__class__.__name__}([])"


# Execute each test for all combinations of these parameter values.
pytestmark = [
    pytest.mark.parametrize("Deque", [LinkedListDeque]),
    pytest.mark.parametrize(
        "items", ["abcd", [3, 2, 1], (True, False, None), range(20)]
    ),
]

# Test the creation method.


def test_init_empty(Deque: type[DequeADT], items: Sequence) -> None:  # noqa: N803 ARG001
    """Test the creation of empty deques. Ignore the items for this test."""
    check_is_empty(Deque())


# Test each modifier method separately.


def test_add_front(Deque: type[DequeADT], items: Sequence) -> None:  # noqa: N803
    """Test that `add_front(item)` adds `item` to the front."""
    deque = Deque()
    for item in items:
        before = deque.size()
        deque.add_front(item)
        assert deque.size() == before + 1
        assert deque.front() == item
        assert deque.back() == items[0]
    assert str(deque) == f"{Deque.__name__}({list(reversed(items))})"


def test_add_back(Deque: type[DequeADT], items: Sequence) -> None:  # noqa: N803
    """Test that `add_back(item)` adds `item` to the back."""
    deque = Deque()
    for item in items:
        before = deque.size()
        deque.add_back(item)
        assert deque.size() == before + 1
        assert deque.front() == items[0]
        assert deque.back() == item
    assert str(deque) == f"{Deque.__name__}({list(items)})"


def test_take_front(Deque: type[DequeADT], items: Sequence) -> None:  # noqa: N803
    """Test that `take_front()` removes and returns the front item."""
    deque = Deque()
    for item in items:
        deque.add_back(item)
    for _ in items:
        before = deque.size()
        assert deque.back() == items[-1]
        assert deque.front() == deque.take_front()
        assert deque.size() == before - 1
    check_is_empty(deque)


def test_take_back(Deque: type[DequeADT], items: Sequence) -> None:  # noqa: N803
    """Test that `take_back()` removes and returns the back item."""
    deque = Deque()
    for item in items:
        deque.add_back(item)
    for _ in items:
        before = deque.size()
        assert deque.front() == items[0]
        assert deque.back() == deque.take_back()
        assert deque.size() == before - 1
    check_is_empty(deque)


# Test the combined behaviour of modifiers.


def test_fifo(Deque: type[DequeADT], items: Sequence) -> None:  # noqa: N803
    """Test that deques can act like queues (first-in first-out)."""
    # Add to the back, take from the front
    deque = Deque()
    for item in items:
        deque.add_back(item)
    for item in items:
        assert deque.take_front() == item
    check_is_empty(deque)
    # Add to the front, take from the back
    for item in items:
        deque.add_front(item)
    for item in items:
        assert deque.take_back() == item
    check_is_empty(deque)


def test_lifo(Deque: type[DequeADT], items: Sequence) -> None:  # noqa: N803
    """Test that deques can act like stacks (last-in first-out)."""
    # Add to the front, take from the front
    deque = Deque()
    for item in items:
        deque.add_front(item)
    for item in reversed(items):
        assert deque.take_front() == item
    check_is_empty(deque)
    # Add to the back, take from the back
    for item in items:
        deque.add_back(item)
    for item in reversed(items):
        assert deque.take_back() == item
    check_is_empty(deque)
