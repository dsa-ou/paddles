"""This module implements the Queue ADT.

## Intuition

The Queue ADT models a line of objects, e.g. cars waiting to board a ferry.
Only the object at the front of the line can be accessed and removed.
The only way to add an object is to put it at the back of the line.

## Definition

A **queue** is a sequence where members are added to one end of the sequence
(the **back** of the queue) and removed from the other end (the **front** of the queue).

A queue is a **first-in, first-out (FIFO)** sequence:
the members are removed in the same order they were added.

A queue is a sequence ordered by age (time of addition).
The oldest member is at the front of the queue, and the youngest member is at the back.

## Operations

The Queue ADT provides operations to:
- create a new empty queue
- add a new member, at the back of the existing ones
- remove the member at the front of the queue
- access the member at the front of the queue without removing it
- compute the size of the queue (number of members).

## Applications

Queues are used to implement breadth-first search.
You should consider using a queue when you need to:
- simulate a real-life queue, like travellers at passport control or
  documents in a printer queue
- process items in the same order they were added, like a to-do list.

## Implementations

The Queue ADT can be implemented with circular dynamic arrays or singly-linked lists.
In both cases, the operations listed above take constant time.
A singly-linked list uses much more memory than a static array of the same length,
but a dynamic array may have wasted capacity and requires resizing.
`paddles` only provides a singly-linked list implementation for the moment.

## Practice

LeetCode has several [problems about queues](https://leetcode.com/tag/queue).
You can sort or filter the problems by difficulty or other criteria,
using the up/down or funnel buttons above the list of problems.
Clicking on the up/down button and then on 'Tags' will show
the algorithmic techniques and ADTs related to each problem.
"""

from collections.abc import Sequence
from typing import Any

__all__ = ["LinkedListQueue"]

# Each linked list node is a list [member, next].
# These constants make the code more readable.
DATA = 0
NEXT = 1


class LinkedListQueue:
    """An implementation of the Queue ADT, using a singly-linked list.

    Besides the ADT's operations, this class provides two convenience operations:
    - create a non-empty queue from a given sequence
    - convert a queue to a string, to see its members listed from front to back.

    >>> from paddles import LinkedListQueue
    >>> q = LinkedListQueue("abc")  # create a non-empty queue
    >>> q.size()                    # number of members
    3
    >>> q.dequeue()                 # remove and return the front member
    'a'
    >>> q.front()                   # return but don't remove the front member
    'b'
    >>> q.enqueue("d")              # add a new member at the back
    >>> print(q)                    # str(q) also possible
    LinkedListQueue(['b', 'c', 'd'])
    """

    def __init__(self, sequence: Sequence[Any] = []) -> None:
        """Initialize the queue with the members of `sequence`.

        The members are added to the queue in the order they are in `sequence`.
        To create an empty queue, call `LinkedListQueue()` or `LinkedListQueue([])`.

        Complexity: O(n), with n = `len(sequence)`
        """
        self._head = None
        self._tail = None
        self._length = 0
        if sequence:
            for item in sequence:
                self.enqueue(item)

    def __str__(self) -> str:
        """Return a string representation of the queue.

        The string is 'LinkedListQueue([front member, ..., back member])'.

        Complexity: O(n), with n = `self.size()`
        """
        strings = []
        current = self._head
        while current:
            strings.append(repr(current[DATA]))
            current = current[NEXT]
        return f"LinkedListQueue([{', '.join(strings)}])"

    def size(self) -> int:
        """Return how many members the queue has.

        Complexity: O(1)
        """
        return self._length

    def front(self) -> Any:
        """Return the member at the front of the queue, without removing it.

        Raise `ValueError` if the queue is empty.

        Complexity: O(1)
        """
        if self.size() == 0:
            msg = "can't access the front of an empty queue"
            raise ValueError(msg)
        return self._head[DATA]

    def enqueue(self, item: Any) -> None:
        """Put `item` at the back of the queue.

        Complexity: O(1)
        """
        node = [item, None]
        if self.size() == 0:
            self._head = node
            self._tail = node
        else:
            self._tail[NEXT] = node
            self._tail = node
        self._length += 1

    def dequeue(self) -> Any:
        """Remove and return the member at the front of the queue.

        Raise `ValueError` if the queue is empty.

        Complexity: O(1)
        """
        if self.size() == 0:
            msg = "can't dequeue from an empty queue"
            raise ValueError(msg)
        item = self._head[DATA]
        self._head = self._head[NEXT]
        self._length -= 1
        if self.size() == 0:
            self._tail = None
        return item
