"""This module implements sorting algorithms.

## Intuition

Sorting is the process of putting items in a specific order,
according to some criterion.

## Definition

A **sorting algorithm** puts members of a collection in a certain order,
according to a criterion usually given by a **comparison function**.
To sort a collection, its members must be **comparable** with each other.
A sorting algorithm may return a new sorted sequence with the input's members,
or it may modify an input sequence **in-place**, rearranging its members.

**Stable** sorting algorithms keep items that compare equal in their original order.

An **adaptive** sorting algorithm takes advantage of existing order in its input.
Adaptive algorithms do the least work if the input is already sorted.

## Operations

This module provides two kinds of functions:
- those named `..._sort` take a Python list and sort it in-place
- those named `..._sorted` take any iterable collection and return a new sorted list.

The aim of this module is not to provide flexible sorting functions,
that can sort in ascending or descending order, using a custom comparison function.
The aim is to convey the algorithms as clearly as possible, keeping the code simple.
Therefore, all functions only sort in **non-descending order**,
with Python's `<=` operator.

## Applications

Sorting is a fundamental computational operation, as it makes items easier to look up,
e.g. trains are listed by arrival or departure time, people are listed by name, etc.
You should consider sorting a collection when you repeatedly need to search it.

## Problems

LeetCode has several [problems about sorting](https://leetcode.com/tag/sorting).
Click twice on 'Difficulty' to sort them from easy to hard.
Click on 'Show problem tags' to see what ADTs they require.
"""

__all__ = ["tim_sort"]


def tim_sort(items: list) -> None:
    """Put `items` in non-descending order, in-place, using TimSort.

    [TimSort](https://en.wikipedia.org/wiki/Timsort) is Python's sorting algorithm,
    derived from Insertion Sort and Merge Sort. It is adaptive and stable.

    Complexity: worst O(n log n), best O(n), with n = len(items)
    """
    items.sort()
