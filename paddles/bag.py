"""This module implements the Bag (Multiset) ADT.

## Intuition

The Bag ADT models a 'bunch' of objects, e.g. a bag of marbles.

## Definition

A **bag** (also called **multiset**) is an unordered collection of members,
possibly with duplicates.
The number of times each member occurs is called its **frequency**.

## Operations

The Bag ADT provides operations to:
- create a new empty bag
- add one copy of a new or of an existing member
- remove one copy of an existing member
- count how many copies of a given item are in the bag (0 if it isn't)
- compute the size of the bag (total number of copies)
- compute the union of bags A and B: if an item occurs *x* times in A
  and *y* times in B, then it occurs max(*x*, *y*) times in the union
- compute the intersection of bags A and B: if an item occurs *x* times in A
  and *y* times in B, then it occurs min(*x*, *y*) times in the intersection
- compute the difference of bags A and B: if an item occurs *x* times in A
  and *y* times in B, then it occurs max(*x* - *y*, 0) times in the difference

## Applications

Bags are used to count how often each item occurs,
e.g. how many times each word appears in a text.

## Implementations

A bag can be represented as a map of items to their frequency.
The map can be implemented with a hash table (if items are hashable) or
with a binary search tree (if items are comparable).
`paddles` only provides a hash table implementation for the moment.
"""

from collections.abc import Hashable, Iterable

__all__ = ["HashTableBag"]


class HashTableBag:
    """An implementation of the Bag ADT with a Python dictionary.

    Besides the ADT's basic operations, for convenience this class allows to:
    - create a non-empty bag from an iterable collection of items
    - convert a bag to a string, to see its members and their frequency
    - check membership, i.e. whether a bag contains a given item
    - add or remove more than one copy of an item at once

    >>> from paddles.bag import HashTableBag
    >>> text = HashTableBag("picnic")               # create a non-empty bag
    >>> text.size()                                 # number of members
    6
    >>> text.frequency("c")
    2
    >>> text.add("a", 3)                            # add 3 copies of "a"
    >>> text.remove("c")                            # remove 1 copy of "c"
    >>> print(text)                                 # str(bag) also possible
    HashTableBag({'p': 1, 'i': 2, 'c': 1, 'n': 1, 'a': 3})
    >>> text.has("T")
    False
    >>> vowels = HashTableBag("aeiou")
    >>> print(text.union(vowels))                   # characters in text or vowels
    HashTableBag({'p': 1, 'i': 2, 'c': 1, 'n': 1, 'a': 3, 'e': 1, 'o': 1, 'u': 1})
    >>> print(text.intersection(vowels))            # vowels that are in text
    HashTableBag({'i': 1, 'a': 1})
    >>> print(vowels.difference(text))              # vowels that aren't in text
    HashTableBag({'e': 1, 'o': 1, 'u': 1})
    """

    def __init__(self, items: Iterable[Hashable] = []) -> None:
        """Initialize the bag with the `items`.

        To create an empty bag, call `HashTableBag()`.
        If `items` is a dictionary, only its keys are added to the bag.

        Complexity: O(len(`items`))
        """
        self._members = {}
        for item in items:
            self.add(item)

    def __str__(self) -> str:
        """Return a string representation of the bag.

        The string is 'HashTableBag({member: copies, ...})'.
        The members are listed in the order they were added to the bag.

        Complexity: O(n), where n is the number of unique items in the bag.
        """
        return f"HashTableBag({self._members})"

    def add(self, item: Hashable, copies: int = 1) -> None:
        """Add the given number of copies of `item` to the bag.

        If omitted, `copies` defaults to 1.
        Raise `ValueError` if `copies` is not positive.

        Complexity: O(1)
        """
        if copies < 1:
            msg = "must add at least one copy"
            raise ValueError(msg)
        if item in self._members:
            self._members[item] += copies
        else:
            self._members[item] = copies

    def remove(self, item: Hashable, copies: int = 1) -> None:
        """Remove the given number of copies of `item` from the bag.

        Raise `ValueError` if `copies < 1` or `self.frequency(item) < copies`.

        Complexity: O(1)
        """
        if copies < 1:
            msg = "must remove at least one copy"
            raise ValueError(msg)
        if self.frequency(item) < copies:
            msg = "can't remove more copies than the bag has"
            raise ValueError(msg)
        self._members[item] -= copies
        if self._members[item] == 0:
            del self._members[item]

    def frequency(self, item: Hashable) -> int:
        """Return how many times `item` occurs in the bag.

        Complexity: O(1)
        """
        if item in self._members:
            return self._members[item]
        return 0

    def has(self, item: Hashable) -> bool:
        """Check if `item` is in the bag.

        Complexity: O(1)
        """
        return item in self._members

    def size(self) -> int:
        """Return how many members (total copies) the bag has.

        Complexity: O(n), where n is the number of unique items in the bag.
        """
        total = 0
        for item in self._members:
            total += self._members[item]
        return total

    def unique(self) -> set:
        """Return the set of the unique members in the bag.

        Complexity: O(n), where n is the number of unique items in the bag.
        """
        return set(self._members)

    def union(self, other: "HashTableBag") -> "HashTableBag":
        """Return a new bag with the items that occur in either bag.

        The frequency of `item` in the union is
        `max(self.frequency(item), other.frequency(item))`.

        Complexity: O(s + o), where s and o are the number of unique items in
        this bag and `other`, respectively.
        """
        new_bag = HashTableBag()
        for item in self.unique() | other.unique():
            new_bag.add(item, max(self.frequency(item), other.frequency(item)))
        return new_bag

    def intersection(self, other: "HashTableBag") -> "HashTableBag":
        """Return a new bag with the common members of this bag and `other`.

        The frequency of `item` in the intersection is
        `min(self.frequency(item), other.frequency(item))`.

        Complexity: O(s + o), where s and o are the number of unique items in
        this bag and `other`, respectively.
        """
        new_bag = HashTableBag()
        for item in self.unique() & other.unique():
            new_bag.add(item, min(self.frequency(item), other.frequency(item)))
        return new_bag

    def difference(self, other: "HashTableBag") -> "HashTableBag":
        """Return a new bag with the members of this bag that aren't in `other`.

        Complexity: O(n), with n the number of unique items in this bag
        """
        new_bag = HashTableBag()
        # The difference is the 'extra' occurrences beyond those in `other`.
        for member in self._members:
            copies = self.frequency(member) - other.frequency(member)
            if copies > 0:
                new_bag.add(member, copies)
        return new_bag

    def equal_to(self, other: "HashTableBag") -> bool:
        """Check if this bag has the same members as `other`.

        Complexity: O(n), with n the number of unique items in this bag
        """
        for member in self._members:
            if self.frequency(member) != other.frequency(member):
                return False
        return self.size() == other.size()  # other can't have extra members

    def included_in(self, other: "HashTableBag") -> bool:
        """Check if all members of this bag are members of `other`.

        Complexity: O(n), with n the number of unique items in this bag
        """
        for member in self._members:
            if self.frequency(member) > other.frequency(member):
                return False
        return True
