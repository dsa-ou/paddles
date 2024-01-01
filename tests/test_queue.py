"""Closed-box unit tests for all Queue ADT implementations."""

from collections.abc import Sequence

import pytest

from paddles.queue import LinkedListQueue

# Helper functions: can't be named test_... or pytest will call them directly.

QueueADT = LinkedListQueue


def check_is_empty(queue: QueueADT) -> None:
    """Test that the queue is empty."""
    assert queue.size() == 0
    with pytest.raises(ValueError, match="can't access front of an empty queue"):
        queue.front()
    with pytest.raises(ValueError, match="can't dequeue from an empty queue"):
        queue.dequeue()
    assert str(queue) == f"{queue.__class__.__name__}([])"


# Fixtures: functions that return the data for testing the queue operations.


@pytest.fixture(params=[LinkedListQueue])
def Queue(request: pytest.FixtureRequest) -> type[QueueADT]:  # noqa: N802
    """Return an implementation (a class) to be tested."""
    return request.param


@pytest.fixture(params=["abcd", [1, 2, 3], (True, False, None), range(20)])
def sequence(request: pytest.FixtureRequest) -> Sequence:
    """Return a sequence of items to test with."""
    return request.param


# Test the creation method.


def test_init_empty(Queue: type[QueueADT]) -> None:  # noqa: N803
    """Test the creation of empty queues."""
    check_is_empty(Queue())


def test_init_iterable(Queue: type[QueueADT], sequence: Sequence) -> None:  # noqa: N803
    """Test the creation of queues from sequences."""
    queue = Queue(sequence)
    assert queue.size() == len(sequence)
    assert queue.front() == sequence[0]
    assert str(queue) == f"{Queue.__name__}({list(sequence)})"


# Test each modifier method separately.


def test_enqueue(Queue: type[QueueADT], sequence: Sequence) -> None:  # noqa: N803
    """Test that `enqueue(item)` adds `item` to the back."""
    queue = Queue()
    for item in sequence:
        before = queue.size()
        queue.enqueue(item)
        assert queue.size() == before + 1
        assert queue.front() == sequence[0]
    assert str(queue) == f"{Queue.__name__}({list(sequence)})"


def test_dequeue(Queue: type[QueueADT], sequence: Sequence) -> None:  # noqa: N803
    """Test that `dequeue()` removes and returns the front item."""
    queue = Queue(sequence)
    for _ in sequence:
        before = queue.size()
        assert queue.front() == queue.dequeue()
        assert queue.size() == before - 1
    check_is_empty(queue)


# Test the combined behaviour of modifiers.


def test_fifo(Queue: type[QueueADT], sequence: Sequence) -> None:  # noqa: N803
    """Test the first-in first-out behaviour of the queue."""
    queue = Queue()
    for item in sequence:
        queue.enqueue(item)
    for item in sequence:
        assert queue.dequeue() == item
    check_is_empty(queue)
