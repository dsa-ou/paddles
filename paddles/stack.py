from collections.abc import Sequence
from typing import Any


class DynamicArrayStack:
    """A stack implementation using Python lists.

    >>> stack = DynamicArrayStack("abc")
    >>> stack.size()
    3
    >>> stack.pop()
    'c'
    >>> stack.peek()
    'b'
    >>> stack.push("C")
    >>> print(stack)
    DynamicArrayStack(['a', 'b', 'C'])
    """

    def __init__(self, iterable: Sequence[Any] | None = None) -> None:
        """Initialize this stack with the given items, if any."""
        if iterable:
            self._members = list(iterable)
        else:
            self._members = []

    def __str__(self) -> str:
        """Return a string representation of this stack.

        The string is 'DynamicArrayStack([bottom member, ..., top member])'.
        """
        return f"DynamicArrayStack({self._members})"

    def size(self) -> int:
        """Return how many members this stack has."""
        return len(self._members)

    def push(self, item: Any) -> None:
        """Add the given item to the top of this stack."""
        self._members.append(item)

    def pop(self) -> Any:
        """Remove and return the top item of this stack.

        Raise ValueError if this stack is empty.
        """
        if self.size() == 0:
            msg = "can't pop a member from an empty stack"
            raise ValueError(msg)
        return self._members.pop()

    def peek(self) -> Any:
        """Return the top item of this stack.

        Raise ValueError if this stack is empty.
        """
        if self.size() == 0:
            msg = "can't peek into an empty stack"
            raise ValueError(msg)
        return self._members[-1]


# Each linked list node is a tuple (data, next).
# These constants make the code more readable.
DATA = 0
NEXT = 1


class LinkedListStack:
    """A stack implementation using singly-linked lists.

    >>> stack = LinkedListStack("abc")
    >>> stack.size()
    3
    >>> stack.pop()
    'c'
    >>> stack.peek()
    'b'
    >>> stack.push("C")
    >>> print(stack)
    LinkedListStack(['a', 'b', 'C'])
    """

    def __init__(self, iterable: Sequence[Any] | None = None) -> None:
        """Initialize this stack with the given items, if any."""
        self._head = None
        self._length = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def __str__(self) -> str:
        """Return a string representation of this stack.

        The string is 'LinkedListStack([bottom member, ..., top member])'.
        """
        strings = []
        current = self._head
        while current:
            strings.append(repr(current[DATA]))
            current = current[NEXT]
        return "LinkedListStack([" + ", ".join(reversed(strings)) + "])"

    def size(self) -> int:
        """Return how many members this stack has."""
        return self._length

    def push(self, item: Any) -> None:
        """Add the given item to the top of this stack."""
        self._head = (item, self._head)
        self._length += 1

    def pop(self) -> Any:
        """Remove and return the item on the top of this stack.

        Raise ValueError if this stack is empty.
        """
        if self.size() == 0:
            msg = "can't pop a member from an empty stack"
            raise ValueError(msg)
        item = self._head[DATA]
        self._head = self._head[NEXT]
        self._length -= 1
        return item

    def peek(self) -> Any:
        """Return the item on the top of this stack.

        Raise ValueError if this stack is empty.
        """
        if self.size() == 0:
            msg = "can't peek into an empty stack"
            raise ValueError(msg)
        return self._head[DATA]
