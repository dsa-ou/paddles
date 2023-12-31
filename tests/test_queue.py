"""Closed-box unit tests for all Queue ADT implementations."""

import pytest

from paddles.queue import LinkedListQueue

# Helper functions: can't be named test_... or pytest will call them directly.


def check_is_empty(queue):
    """Test that the queue is empty."""
    assert queue.size() == 0
    with pytest.raises(ValueError):
        queue.front()
    with pytest.raises(ValueError):
        queue.dequeue()
    assert str(queue) == f"{queue.__class__.__name__}([])"


# Fixtures: functions that return the data for testing the queue operations.


@pytest.fixture(params=[LinkedListQueue])
def Queue(request):
    """Return an implementation (a class) to be tested."""
    return request.param


@pytest.fixture(params=["abcd", [1, 2, 3], (True, False, None), range(20)])
def sequence(request):
    """Return a sequence of items to test with."""
    return request.param


# Test the creation method.


def test_init_empty(Queue):
    """Test the creation of empty queues."""
    check_is_empty(Queue())


def test_init_iterable(Queue, sequence):
    """Test the creation of queues from sequences."""
    queue = Queue(sequence)
    assert queue.size() == len(sequence)
    assert queue.front() == sequence[0]
    assert str(queue) == f"{Queue.__name__}({list(sequence)})"


# Test each modifier method separately.


def test_enqueue(Queue, sequence):
    """Test that `enqueue(item)` adds `item` to the back."""
    queue = Queue()
    for item in sequence:
        before = queue.size()
        queue.enqueue(item)
        assert queue.size() == before + 1
        assert queue.front() == sequence[0]
    assert str(queue) == f"{Queue.__name__}({list(sequence)})"


def test_dequeue(Queue, sequence):
    """Test that `dequeue()` removes and returns the front item."""
    queue = Queue(sequence)
    for _ in sequence:
        before = queue.size()
        assert queue.front() == queue.dequeue()
        assert queue.size() == before - 1
    check_is_empty(queue)


# Test the combined behaviour of modifiers.


def test_fifo(Queue, sequence):
    """Test the first-in first-out behaviour of the queue."""
    queue = Queue()
    for item in sequence:
        queue.enqueue(item)
    for item in sequence:
        assert queue.dequeue() == item
    check_is_empty(queue)
