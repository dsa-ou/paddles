"""Closed-box unit tests for all sorting algorithms."""

from collections.abc import Callable, Iterable

import pytest

from paddles.sorting import *

# Functions named `..._sort` take a list and sort it in place.
SortFunction = Callable[[list], None]
# Functions named `..._sorted` take an iterable collection and return a new sorted list.
SortedFunction = Callable[[Iterable], list]


# fmt: off
LISTS = [
    [],                             # empty list
    [5],                            # singleton list
    [1, 2, 3, 4, 5],                # already ascending
    [5, 4, 3, 2, 1],                # reverse order
    [0] * 10,                       # all equal
    [-5, -4, 3, 1, 0, 3, 3, 0],     # ascending and descending runs
    [1, 5, 2, 4, 3, 1],             # up and down
]

OTHER = [
    set(), (), {}, "",              # empty collections
    {5}, (5,), {True: None}, "?",   # singletons
    (-1, 3, 5, 7), "abcdef",        # already ascending
    (8, 6, 4, 2), "fedcba",         # reverse order
    (0,) * 10, "...",               # all equal
    {5, 3, 4, 2}, {5, 4, 2, 3},     # sets
    {3: None, -1: True, 2: False},  # dictionary with comparable keys
]
# "A (very) short sentence.",     # string with repeated characters  # noqa: ERA001
# fmt: on

# Test the sorting algorithms.


@pytest.mark.parametrize("sort_function", [bogo_sort, bubble_sort, selection_sort])
@pytest.mark.parametrize("to_sort", LISTS)
def test_sort(sort_function: SortFunction, to_sort: list) -> None:
    """Test a function that sorts a list in-place with the items to sort."""
    # Copy the input, so that subsequent functions don't get already sorted lists.
    copied = list(to_sort)
    sort_function(copied)
    assert copied == sorted(to_sort)


@pytest.mark.parametrize("sorted_function", [bogo_sorted])
@pytest.mark.parametrize("to_sort", LISTS + OTHER)
def test_sorted(sorted_function: SortedFunction, to_sort: Iterable) -> None:
    """Test a function that returns a new sorted list with the items to sort."""
    assert sorted_function(to_sort) == sorted(to_sort)
