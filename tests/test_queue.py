"""Closed-box unit tests for all Queue ADT implementations."""

from collections.abc import Sequence

import pytest

from paddles import LinkedListQueue

# Helper functions: can't be named test_... or pytest will call them directly.

QueueADT = LinkedListQueue


def check_is_empty(queue: QueueADT) -> None:
    """Test that the queue is empty."""
    assert queue.size() == 0
    with pytest.raises(ValueError, match="can't access the front of an empty queue"):
        queue.front()
    with pytest.raises(ValueError, match="can't dequeue from an empty queue"):
        queue.dequeue()
    assert str(queue) == f"{queue.__class__.__name__}([])"


# Execute each test for all combinations of these parameter values.
pytestmark = [
    pytest.mark.parametrize("Queue", [LinkedListQueue]),
    pytest.mark.parametrize(
        "items", ["abcd", [3, 2, 1], (True, False, None), range(20)]
    ),
]


# Test the creation method.


def test_init_empty(Queue: type[QueueADT], items: Sequence) -> None:  # noqa: N803 ARG001
    """Test the creation of empty queues. Ignore the items."""
    check_is_empty(Queue())


def test_init_iterable(Queue: type[QueueADT], items: Sequence) -> None:  # noqa: N803
    """Test the creation of queues from itemss."""
    queue = Queue(items)
    assert queue.size() == len(items)
    assert queue.front() == items[0]
    assert str(queue) == f"{Queue.__name__}({list(items)})"


# Test each modifier method separately.


def test_enqueue(Queue: type[QueueADT], items: Sequence) -> None:  # noqa: N803
    """Test that `enqueue(item)` adds `item` to the back."""
    queue = Queue()
    for item in items:
        before = queue.size()
        queue.enqueue(item)
        assert queue.size() == before + 1
        assert queue.front() == items[0]
    assert str(queue) == f"{Queue.__name__}({list(items)})"


def test_dequeue(Queue: type[QueueADT], items: Sequence) -> None:  # noqa: N803
    """Test that `dequeue()` removes and returns the front item."""
    queue = Queue(items)
    for _ in items:
        before = queue.size()
        assert queue.front() == queue.dequeue()
        assert queue.size() == before - 1
    check_is_empty(queue)


# Test the combined behaviour of modifiers.


def test_fifo(Queue: type[QueueADT], items: Sequence) -> None:  # noqa: N803
    """Test the first-in first-out behaviour of the queue."""
    queue = Queue()
    for item in items:
        queue.enqueue(item)
    for item in items:
        assert queue.dequeue() == item
    check_is_empty(queue)
