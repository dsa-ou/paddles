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

A **stable** sorting algorithm keeps items that compare equal in their original order.

An **adaptive** sorting algorithm takes advantage of existing order in its input.
Adaptive algorithms do the least work if the input is already sorted.

## Operations

This module provides two kinds of functions:
- those named `..._sort` take a Python list and sort it in-place
- those named `..._sorted` take a sequence and return a new sorted list.

The aim of this module is not to provide flexible sorting functions,
that can sort in ascending or descending order, using a custom comparison function.
The aim is to convey the algorithms as clearly as possible, keeping the code simple.
Therefore, all functions only sort in **non-descending order**,
with Python's `<=` operator.

## Applications

Sorting is a fundamental computational operation, as it makes items easier to look up,
e.g. trains are listed by arrival or departure time, people are listed by name, etc.
You should consider sorting a collection when you repeatedly need to search it.

## Implementations

Function | In-place | Stable | Adaptive | Worst Time Complexity
- | :-: | :-: | :-: | :-:
`bogo_sort` | ✔️ | | | O(∞)
`bogo_sorted` | | | | O(n·n!)
`bubble_sort` | ✔️ | ✔️ | ✔️ | O(n²)
`insertion_sort` | ✔️ | ✔️ | ✔️ | O(n²)
`merge_sorted` | | ✔️ | | O(n log n)
`quick_sorted` | | ✔️ | | O(n²)
`quick_sorted_3way` | | ✔️ | | O(n²)
`selection_sort` | ✔️ | | | O(n²)

Other functions:
- `quick_select`: find the k-th smallest item with a variant of `quick_sorted`

## Practice

LeetCode has several [problems about sorting](https://leetcode.com/tag/sorting).
You can sort or filter the problems by difficulty or other criteria,
using the up/down or funnel buttons above the list of problems.
Clicking on the up/down button and then on 'Tags' will show
the algorithmic techniques and ADTs related to each problem.
"""

__all__ = [
    "bogo_sort",
    "bogo_sorted",
    "bubble_sort",
    "insertion_sort",
    "merge_sorted",
    "quick_select",
    "quick_sorted",
    "quick_sorted_3way",
    "selection_sort",
]

import itertools
import random
from collections.abc import Sequence


def is_non_decreasing(items: Sequence) -> bool:
    """Check if `items[0] <= items[1] <= ... <= items[-1]`."""
    for index in range(len(items) - 1):
        if items[index] > items[index + 1]:
            return False
    return True


def bogo_sort(items: list) -> None:
    """Put `items` in non-descending order, in-place, using Bogo Sort.

    Non-deterministic [Bogo Sort](https://en.wikipedia.org/wiki/Bogosort)
    repeatedly shuffles the items until they are in the right order.

    Complexity: O(∞) as the algorithm may not terminate
    """
    while not is_non_decreasing(items):
        random.shuffle(items)


def bogo_sorted(items: Sequence) -> list:  # ty: ignore[invalid-return-type] # noqa: RET503
    """Return a new list with `items` in non-descending order, using Bogo Sort.

    Deterministic [Bogo Sort](https://en.wikipedia.org/wiki/Bogosort)
    exhaustively searches for a permutation of items that is in the right order.

    Complexity: O(n·n!) with n = `len(items)`
    """
    # Type checkers and linters assume the for-loop may be skipped, returning None.
    # The `ty` and `noqa` comments above remove such error messages.
    for permutation in itertools.permutations(items):
        # Each generated permutation is a tuple, not a list.
        if is_non_decreasing(permutation):
            return list(permutation)


def bubble_sort(items: list) -> None:
    """Put `items` in non-descending order, in-place, using Bubble Sort.

    [Bubble Sort](https://en.wikipedia.org/wiki/Bubble_sort) repeatedly
    swaps adjacent items that are in the wrong order.

    Complexity: O(n²), with n = `len(items)`
    """
    for scan in range(1, len(items)):
        swapped = False
        for index in range(len(items) - scan):
            if items[index] > items[index + 1]:
                current = items[index]
                items[index] = items[index + 1]
                items[index + 1] = current
                swapped = True
        if not swapped:
            return


def insertion_sort(items: list) -> None:
    """Put `items` in non-descending order, in-place, using Insertion Sort.

    [Insertion Sort](https://en.wikipedia.org/wiki/Insertion_sort) repeatedly
    inserts the next unsorted item into its correct position in the sorted part.

    Complexity: O(n²), with n = `len(items)`
    """
    for first_unsorted in range(1, len(items)):
        to_sort = items[first_unsorted]
        index = first_unsorted
        while index > 0 and items[index - 1] > to_sort:
            items[index] = items[index - 1]
            index = index - 1
        items[index] = to_sort


def merge(left: Sequence, right: Sequence) -> list:
    """Return a new non-decreasing list by merging two non-decreasing sequences."""
    left_index = 0
    right_index = 0
    merged = []
    while left_index < len(left) and right_index < len(right):
        left_item = left[left_index]
        right_item = right[right_index]
        if left_item < right_item:
            merged.append(left_item)
            left_index = left_index + 1
        else:
            merged.append(right_item)
            right_index = right_index + 1
    for index in range(left_index, len(left)):
        merged.append(left[index])  # noqa: PERF401
    for index in range(right_index, len(right)):
        merged.append(right[index])  # noqa: PERF401
    return merged


def merge_sorted(items: Sequence) -> list:
    """Return a new list with `items` in non-decreasing order, using Merge Sort.

    [Merge Sort](https://en.wikipedia.org/wiki/Merge_sort)
    divides the list into two halves, recursively sorts each one, and merges them.

    Complexity: O(n log n) with n = `len(items)`
    """
    if len(items) < 2:  # noqa: PLR2004
        return list(items)
    middle = len(items) // 2
    left_sorted = merge_sorted(items[:middle])
    right_sorted = merge_sorted(items[middle:])
    return merge(left_sorted, right_sorted)


def quick_sorted(items: Sequence) -> list:
    """Return a new list with `items` in non-decreasing order, using Quick Sort.

    [Quick Sort](https://en.wikipedia.org/wiki/Quicksort) selects a pivot,
    partitions the items around it, and recursively sorts the partitions.

    Complexity: O(n²), with n = `len(items)`
    """
    # base case: sequences with 0 or 1 items are sorted
    if len(items) < 2:  # noqa: PLR2004
        return list(items)
    # reduce: select the pivot and create two partitions
    smaller = []
    larger = []
    pivot = items[0]
    for index in range(1, len(items)):
        item = items[index]
        if item < pivot:
            smaller.append(item)
        else:
            larger.append(item)
    # recur: sort each partition
    # combine: concatenate the sorted partitions, with the pivot in between
    return quick_sorted(smaller) + [pivot] + quick_sorted(larger)  # noqa: RUF005


def quick_sorted_3way(items: Sequence) -> list:
    """Return a new list with `items` in non-decreasing order, using 3-way Quick Sort.

    [3-way Quick Sort](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)
    partitions the items into three groups: smaller, equal, and larger than the pivot.

    Complexity: O(n²), with n = `len(items)`
    """
    if len(items) < 2:  # noqa: PLR2004
        return list(items)
    # reduce: partition the items into three groups according to a random pivot
    pivot = random.choice(items)  # noqa: S311
    smaller = []
    equal = []
    larger = []
    for item in items:
        if item < pivot:
            smaller.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            larger.append(item)
    # recur: sort the smaller and larger groups
    # combine: concatenate the sorted groups
    return quick_sorted_3way(smaller) + equal + quick_sorted_3way(larger)


def quick_select(items: Sequence, k: int) -> object:
    """Return the `k`-th smallest item in `items`, using Quick Select.

    [Quick Select](https://en.wikipedia.org/wiki/Quickselect) is a variant of Quick Sort
    that only recurses into the partition that contains the k-th smallest item.

    Raise `ValueError` if `k` isn't a value from 1 to `len(items)`.

    Complexity: O(n²), with n = `len(items)`
    """
    if not (0 < k <= len(items)):
        msg = f"Cannot select {k}th smallest item from {len(items)} items"  # noqa: S608
        raise ValueError(msg)
    # reduce: select the pivot and create two partitions
    smaller = []
    larger = []
    pivot = items[0]
    for index in range(1, len(items)):
        item = items[index]
        if item < pivot:
            smaller.append(item)
        else:
            larger.append(item)
    # recur: select the partition that contains the k-th smallest item
    if k <= len(smaller):
        return quick_select(smaller, k)
    if k == len(smaller) + 1:
        return pivot
    return quick_select(larger, k - (len(smaller) + 1))


def selection_sort(items: list) -> None:
    """Put `items` in non-descending order, in-place, using Selection Sort.

    [Selection Sort](https://en.wikipedia.org/wiki/Selection_sort) repeatedly
    selects the smallest unsorted item and moves it to the end of the sorted part.

    Complexity: O(n²) with n = `len(items)`
    """
    for first_unsorted in range(len(items) - 1):
        # find the index of the smallest item among the unsorted ones
        smallest = first_unsorted
        for index in range(smallest + 1, len(items)):
            if items[index] < items[smallest]:
                smallest = index
        # swap the smallest unsorted item with the first unsorted item
        unsorted_item = items[first_unsorted]
        items[first_unsorted] = items[smallest]
        items[smallest] = unsorted_item
