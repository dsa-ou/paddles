"""This module implements the Deque ADT.

## Intuition

The Deque ADT models a line of objects that can be accessed, added to and
removed from either end of the line.
A deque can be used as a [stack](stack.html) or as a [queue](queue.html).

## Definition

A **deque**, pronounced 'deck' and short for 'double-ended queue', is a sequence
where only the members at both ends of the sequence
(called the **front** and the **back** of the queue) can be accessed and removed.
New members can only be added at the front or at the back.

## Operations

The Deque ADT provides operations to:
- create a new empty deque
- add a new member to the front of the deque
- add a new member to the back of the deque
- remove the member at the front of the deque
- remove the member at the back of the deque
- access the member at the front of the deque without removing it
- access the member at the back of the deque without removing it
- compute the size of the deque (number of members).

## Applications

Consider using a deque when you need to simulate a queue where
- objects jump the queue (join at the front) or
  leave it from the back after waiting a certain time
- the direction of the queue changes, like cars on a ferry.

## Implementations

The Deque ADT can be implemented with circular dynamic arrays or doubly-linked lists.
In both cases, the operations listed above take constant time.
A doubly-linked list uses much more memory than a static array of the same length,
but a dynamic array may have wasted capacity and requires resizing.
`paddles` only provides a doubly-linked list implementation for the moment.
"""

from collections.abc import Sequence
from typing import Any

__all__ = ["LinkedListDeque"]

# A doubly-linked list node is a list [previous, item, next].
# These constants make the code more readable.
PREV = 0
DATA = 1
NEXT = 2


class LinkedListDeque:
    """An implementation of the Deque ADT, using a doubly-linked list.

    Besides the ADT's operations, this class provides two convenience operations:
    - create a non-empty deque from a given sequence
    - convert a deque to a string, to see its members listed from front to back.

    >>> from paddles import LinkedListDeque
    >>> deque = LinkedListDeque("abc")          # create a non-empty deque
    >>> deque.size()                            # number of members
    3
    >>> deque.take_front()                      # remove and return the front member
    'a'
    >>> deque.take_back()                       # remove and return the back member
    'c'
    >>> deque.front() == deque.back() == 'b'    # return the front and back members
    True
    >>> deque.add_back("C")                     # add a new member at the back
    >>> deque.add_front("A")                    # add a new member at the front
    >>> print(deque)                            # str(deque) also possible
    LinkedListDeque(['A', 'b', 'C'])
    """

    def __init__(self, sequence: Sequence[Any] = []) -> None:
        """Initialize the deque with the members of `sequence`.

        The members are added to the deque in the order they are in `sequence`.
        To create an empty deque, call `LinkedListDeque()` or `LinkedListDeque([])`.

        Complexity: O(len(`sequence`))
        """
        self._head = None
        self._tail = None
        self._length = 0
        if sequence:
            for item in sequence:
                self.add_back(item)

    def __str__(self) -> str:
        """Return a string representation of the deque.

        The string is 'LinkedListDeque([front member, ..., back member])'.

        Complexity: O(self.size())
        """
        strings = []
        current = self._head
        while current:
            strings.append(repr(current[DATA]))
            current = current[NEXT]
        return f"LinkedListDeque([{', '.join(strings)}])"

    def size(self) -> int:
        """Return how many members the deque has.

        Complexity: O(1)
        """
        return self._length

    def front(self) -> Any:
        """Return the item at the front of the deque, without removing it.

        Raise `ValueError` if the deque is empty.

        Complexity: O(1)
        """
        if self.size() == 0:
            msg = "can't access the front of an empty deque"
            raise ValueError(msg)
        return self._head[DATA]

    def back(self) -> Any:
        """Return the item at the back of the deque, without removing it.

        Raise `ValueError` if the deque is empty.

        Complexity: O(1)
        """
        if self.size() == 0:
            msg = "can't access the back of an empty deque"
            raise ValueError(msg)
        return self._tail[DATA]

    def add_front(self, item: Any) -> None:
        """Put `item` at the front of the deque.

        Complexity: O(1)
        """
        node = [None, item, self._head]
        if self.size() == 0:
            self._tail = node
        else:
            self._head[PREV] = node
        self._head = node
        self._length += 1

    def add_back(self, item: Any) -> None:
        """Put `item` at the back of the deque.

        Complexity: O(1)
        """
        node = [self._tail, item, None]
        if self.size() == 0:
            self._head = node
        else:
            self._tail[NEXT] = node
        self._tail = node
        self._length += 1

    def take_front(self) -> Any:
        """Remove and return the item at the front of the deque.

        Raise `ValueError` if the deque is empty.

        Complexity: O(1)
        """
        if self.size() == 0:
            msg = "can't remove a member from an empty deque"
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
        """Remove and return the item at the back of the deque.

        Raise `ValueError` if the deque is empty.

        Complexity: O(1)
        """
        if self.size() == 0:
            msg = "can't remove a member from an empty deque"
            raise ValueError(msg)
        item = self._tail[DATA]
        self._tail = self._tail[PREV]
        self._length -= 1
        if self.size() == 0:
            self._head = None
        else:
            self._tail[NEXT] = None
        return item
