"""This module implements the Stack ADT.

## Intuition

The Stack ADT models a pile of objects, e.g. a pile of storage boxes.
Only the object at the top of the pile can be accessed and removed.
The only way to add an object is to put it on top of the existing pile.

## Definition

A **stack** is a sequence where members are removed from and added to
the same end of the sequence, called the **top** of the stack.

A stack is a **last-in, first-out (LIFO)** sequence:
the next member to be removed is the one most recently added.

A stack is a sequence ordered by age (time of addition).
The oldest member is at the bottom of the stack, and the youngest member is at the top.

## Operations

The Stack ADT provides operations to:
- create a new empty stack
- add a new member, on top of the existing ones
- remove the member at the top of the stack
- access the member at the top of the stack without removing it
- compute the size of the stack (number of members).

## Applications

Stacks are used to implement function calls and depth-first search.
You should consider using a stack when you need to:
- simulate the handling of a pile of objects, like loading and unloading ship containers
- process nested structures, like brackets (e.g. `print([1, {2, 3}])`) or
  HTML tags (e.g. `<p><b>text</b></p>`)
- process items in the reverse order they were added, like undo operations
  (commands are undone in the reverse order they were executed).

## Implementations

A stack can be stored in a dynamic array (see `DynamicArrayStack`)
or a singly-linked list (see `LinkedListStack`).
In both cases, the operations take constant time.
A singly-linked list uses much more memory than a static array of the same length,
but a dynamic array may have wasted capacity and requires resizing.

## Practice

LeetCode has several [problems about stacks](https://leetcode.com/tag/stack).
You can sort or filter the problems by difficulty or other criteria,
using the up/down or funnel buttons above the list of problems.
Clicking on the up/down button and then on 'Tags' will show
the algorithmic techniques and ADTs related to each problem.
"""

from collections.abc import Sequence
from typing import Any

__all__ = ["DynamicArrayStack", "LinkedListStack"]


class DynamicArrayStack:
    """An implementation of the Stack ADT, using Python lists.

    Besides the ADT's operations, this class provides two convenience operations:
    - create a non-empty stack from a given sequence
    - convert a stack to a string, to see its members listed from bottom to top.

    >>> from paddles import DynamicArrayStack
    >>> stack = DynamicArrayStack("abc")    # create a non-empty stack
    >>> stack.size()                        # number of members
    3
    >>> stack.pop()                         # remove and return the top member
    'c'
    >>> stack.peek()                        # return but don't remove the top member
    'b'
    >>> stack.push("C")                     # add a new member on top
    >>> print(stack)                        # str(stack) also possible
    DynamicArrayStack(['a', 'b', 'C'])
    """

    def __init__(self, sequence: Sequence[Any] = []) -> None:
        """Initialize the stack with the members of `sequence`.

        The members are added to the stack in the order they are in `sequence`.
        To create an empty stack, call `DynamicArrayStack()` or `DynamicArrayStack([])`.

        Complexity: O(n), with n = `len(sequence)`
        """
        self._members = []
        for item in sequence:
            self.push(item)

    def __str__(self) -> str:
        """Return a string representation of the stack.

        The string is 'DynamicArrayStack([bottom member, ..., top member])'.

        Complexity: O(n), with n = `self.size()`
        """
        return f"DynamicArrayStack({self._members})"

    def size(self) -> int:
        """Return how many members the stack has.

        Complexity: O(1)
        """
        return len(self._members)

    def peek(self) -> Any:
        """Return the member at the top of the stack, without removing it.

        Raise `ValueError` if the stack is empty.

        Complexity: O(1)
        """
        if self.size() == 0:
            msg = "can't peek into an empty stack"
            raise ValueError(msg)
        return self._members[-1]

    def push(self, item: Any) -> None:
        """Put `item` on top of the stack.

        Complexity: O(1)
        """
        self._members.append(item)

    def pop(self) -> Any:
        """Remove and return the member at the top of the stack.

        Raise `ValueError` if the stack is empty.

        Complexity: O(1)
        """
        if self.size() == 0:
            msg = "can't pop a member from an empty stack"
            raise ValueError(msg)
        return self._members.pop()


# Each linked list node is a tuple (data, next).
# These constants make the code more readable.
DATA = 0
NEXT = 1


class LinkedListStack:
    """An implementation of the Stack ADT, using singly-linked lists.

    Besides the ADT's operations, this class provides two convenience operations:
    - create a non-empty stack from a given sequence
    - convert a stack to a string, to see its members listed from bottom to top.

    >>> from paddles import LinkedListStack
    >>> stack = LinkedListStack("abc")      # create a non-empty stack
    >>> stack.size()                        # number of members
    3
    >>> stack.pop()                         # remove and return the top member
    'c'
    >>> stack.peek()                        # return but don't remove the top member
    'b'
    >>> stack.push("C")                     # add a new member on top
    >>> print(stack)                        # str(stack) also possible
    LinkedListStack(['a', 'b', 'C'])
    """

    def __init__(self, sequence: Sequence[Any] = []) -> None:
        """Initialize the stack with the members of `sequence`.

        The members are added to the stack in the order they are in `sequence`.
        To create an empty stack, call `LinkedListStack()` or `LinkedListStack([])`.

        Complexity: O(n), with n = `len(sequence)`
        """
        self._head = None
        self._length = 0
        for item in sequence:
            self.push(item)

    def __str__(self) -> str:
        """Return a string representation of the stack.

        The string is 'LinkedListStack([bottom member, ..., top member])'.

        Complexity: O(n), with n = `self.size()`
        """
        strings = []
        current = self._head
        while current:
            strings.append(repr(current[DATA]))
            current = current[NEXT]
        return "LinkedListStack([" + ", ".join(reversed(strings)) + "])"

    def size(self) -> int:
        """Return how many members the stack has.

        Complexity: O(1)
        """
        return self._length

    def push(self, item: Any) -> None:
        """Put `item` on top of the stack.

        Complexity: O(1)
        """
        self._head = (item, self._head)
        self._length += 1

    def pop(self) -> Any:
        """Remove and return the member at the top of the stack.

        Raise `ValueError` if the stack is empty.

        Complexity: O(1)
        """
        if self.size() == 0:
            msg = "can't pop a member from an empty stack"
            raise ValueError(msg)
        item = self._head[DATA]
        self._head = self._head[NEXT]
        self._length -= 1
        return item

    def peek(self) -> Any:
        """Return the member at the top of the stack.

        Raise `ValueError` if the stack is empty.

        Complexity: O(1)
        """
        if self.size() == 0:
            msg = "can't peek into an empty stack"
            raise ValueError(msg)
        return self._head[DATA]
