"""Closed-box unit tests for all sorting algorithms."""

from collections.abc import Callable, Iterable, Sequence

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

SEQUENCES = [
    (), "", (5,), "?",              # empty and singletons
    (-1, 3, 5, 7), "abcdef",        # already ascending
    (8, 6, 4, 2), "fedcba",         # reverse order
    (0,) * 10, "...",               # all equal
    (1, 2, 3, 2, 1), "abcbca",      # up and down
]
# "A (very) short sentence.",     # string with repeated characters  # noqa: ERA001
# fmt: on

# Test the sorting algorithms against Python's built-in sorting.


@pytest.mark.parametrize(
    "sort_function", [bogo_sort, bubble_sort, insertion_sort, selection_sort]
)
@pytest.mark.parametrize("to_sort", LISTS)
def test_sort(sort_function: SortFunction, to_sort: list) -> None:
    """Test a function that sorts a list in-place with the items to sort."""
    # Copy the input, so that subsequent functions don't get already sorted lists.
    copied = list(to_sort)
    sort_function(copied)
    assert copied == sorted(to_sort)


@pytest.mark.parametrize(
    "sorted_function", [bogo_sorted, merge_sorted, quick_sorted, quick_sorted_3way]
)
@pytest.mark.parametrize("to_sort", LISTS + SEQUENCES)
def test_sorted(sorted_function: SortedFunction, to_sort: Sequence) -> None:
    """Test a function that returns a new sorted list with the items to sort."""
    assert sorted_function(to_sort) == sorted(to_sort)


@pytest.mark.parametrize("items", LISTS + SEQUENCES)
def test_quick_select(items: Sequence) -> None:
    """Select the k-th smallest item of a non-empty sequence, for all possible k."""
    if items:
        for k, expected in enumerate(sorted(items)):
            assert quick_select(items, k + 1) == expected


@pytest.mark.parametrize("items", LISTS + SEQUENCES)
def test_quick_select_error(items: Sequence) -> None:
    """Test selecting the k-th smallest item of an empty sequence or an invalid k."""
    for k in (-1, 0, len(items) + 1):
        with pytest.raises(ValueError):  # noqa: PT011
            quick_select(items, k)
