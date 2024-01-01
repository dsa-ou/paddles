from collections.abc import Sequence
from typing import Any

# A doubly-linked list node is a list [previous, item, next].
# These constants make the code more readable.
PREV = 0
DATA = 1
NEXT = 2


class LinkedListDeque:
    """Deque implementation using a doubly linked list for storage.

    >>> items = LinkedListDeque("abc")
    >>> print(items)
    LinkedListDeque(['a', 'b', 'c'])
    >>> items.size()
    3
    >>> items.take_front()
    'a'
    >>> items.take_back()
    'c'
    >>> items.front() == items.back() == 'b'
    True
    >>> items.add_back("C")
    >>> items.add_front("A")
    >>> print(items)
    LinkedListDeque(['A', 'b', 'C'])
    """

    def __init__(self, iterable: Sequence[Any] | None = None) -> None:
        """Initialize this deque with the given items, if any."""
        self._head = None
        self._tail = None
        self._length = 0
        if iterable:
            for item in iterable:
                self.add_back(item)

    def __str__(self) -> str:
        """Return a formatted string representation of this deque."""
        strings = []
        current = self._head
        while current:
            strings.append(repr(current[DATA]))
            current = current[NEXT]
        return f"LinkedListDeque([{', '.join(strings)}])"

    def size(self) -> int:
        """Return the number of items in this deque."""
        return self._length

    def add_front(self, item: Any) -> None:
        """Insert the given item at the front of this deque."""
        node = [None, item, self._head]
        if self.size() == 0:
            self._tail = node
        else:
            self._head[PREV] = node
        self._head = node
        self._length += 1

    def add_back(self, item: Any) -> None:
        """Insert the given item at the back of this deque."""
        node = [self._tail, item, None]
        if self.size() == 0:
            self._head = node
        else:
            self._tail[NEXT] = node
        self._tail = node
        self._length += 1

    def take_front(self) -> Any:
        """Remove and return the item at the front of this deque.

        Raise ValueError if this deque is empty.
        """
        if self.size() == 0:
            msg = "can't take from an empty deque"
            raise ValueError(msg)
        item = self._head[DATA]
        self._head = self._head[NEXT]
        self._length -= 1
        if self.size() == 0:
            self._tail = None
        else:
            self._head[PREV] = None
        return item

    def take_back(self) -> Any:
        """Remove and return the item at the back of this deque.

        Raise ValueError if this deque is empty.
        """
        if self.size() == 0:
            msg = "can't take from an empty deque"
            raise ValueError(msg)
        item = self._tail[DATA]
        self._tail = self._tail[PREV]
        self._length -= 1
        if self.size() == 0:
            self._head = None
        else:
            self._tail[NEXT] = None
        return item

    def front(self) -> Any:
        """Return the item at the front of this deque without removing it.

        Raise ValueError if this deque is empty.
        """
        if self.size() == 0:
            msg = "Deque is empty"
            raise ValueError(msg)
        return self._head[DATA]

    def back(self) -> Any:
        """Return the item at the back of this deque without removing it.

        Raise ValueError if this deque is empty.
        """
        if self.size() == 0:
            msg = "Deque is empty"
            raise ValueError(msg)
        return self._tail[DATA]
