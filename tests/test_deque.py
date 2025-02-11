"""Closed-box unit tests for all implementations of the Deque ADT."""

from collections.abc import Sequence

import pytest

from paddles.deque import LinkedListDeque

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
        "sequence", ["abcd", [3, 2, 1], (True, False, None), range(20)]
    ),
]

# Test the creation method.


def test_init_empty(Deque: type[DequeADT], sequence: Sequence) -> None:  # noqa: N803 ARG001
    """Test the creation of empty deques. Ignore the sequence for this test."""
    check_is_empty(Deque())


def test_init_iterable(Deque: type[DequeADT], sequence: Sequence) -> None:  # noqa: N803
    """Test the creation of deques from sequences."""
    deque = Deque(sequence)
    assert deque.size() == len(sequence)
    assert deque.front() == sequence[0]
    assert deque.back() == sequence[-1]
    assert str(deque) == f"{Deque.__name__}({list(sequence)})"


# Test each modifier method separately.


def test_add_front(Deque: type[DequeADT], sequence: Sequence) -> None:  # noqa: N803
    """Test that `add_front(item)` adds `item` to the front."""
    deque = Deque()
    for item in sequence:
        before = deque.size()
        deque.add_front(item)
        assert deque.size() == before + 1
        assert deque.front() == item
        assert deque.back() == sequence[0]
    assert str(deque) == f"{Deque.__name__}({list(reversed(sequence))})"


def test_add_back(Deque: type[DequeADT], sequence: Sequence) -> None:  # noqa: N803
    """Test that `add_back(item)` adds `item` to the back."""
    deque = Deque()
    for item in sequence:
        before = deque.size()
        deque.add_back(item)
        assert deque.size() == before + 1
        assert deque.front() == sequence[0]
        assert deque.back() == item
    assert str(deque) == f"{Deque.__name__}({list(sequence)})"


def test_take_front(Deque: type[DequeADT], sequence: Sequence) -> None:  # noqa: N803
    """Test that `take_front()` removes and returns the front item."""
    deque = Deque(sequence)
    for _ in sequence:
        before = deque.size()
        assert deque.back() == sequence[-1]
        assert deque.front() == deque.take_front()
        assert deque.size() == before - 1
    check_is_empty(deque)


def test_take_back(Deque: type[DequeADT], sequence: Sequence) -> None:  # noqa: N803
    """Test that `take_back()` removes and returns the back item."""
    deque = Deque(sequence)
    for _ in sequence:
        before = deque.size()
        assert deque.front() == sequence[0]
        assert deque.back() == deque.take_back()
        assert deque.size() == before - 1
    check_is_empty(deque)


# Test the combined behaviour of modifiers.


def test_fifo(Deque: type[DequeADT], sequence: Sequence) -> None:  # noqa: N803
    """Test that deques can act like queues (first-in first-out)."""
    # Add to the back, take from the front
    deque = Deque()
    for item in sequence:
        deque.add_back(item)
    for item in sequence:
        assert deque.take_front() == item
    check_is_empty(deque)
    # Add to the front, take from the back
    for item in sequence:
        deque.add_front(item)
    for item in sequence:
        assert deque.take_back() == item
    check_is_empty(deque)


def test_lifo(Deque: type[DequeADT], sequence: Sequence) -> None:  # noqa: N803
    """Test that deques can act like stacks (last-in first-out)."""
    # Add to the front, take from the front
    deque = Deque()
    for item in sequence:
        deque.add_front(item)
    for item in reversed(sequence):
        assert deque.take_front() == item
    check_is_empty(deque)
    # Add to the back, take from the back
    for item in sequence:
        deque.add_back(item)
    for item in reversed(sequence):
        assert deque.take_back() == item
    check_is_empty(deque)
