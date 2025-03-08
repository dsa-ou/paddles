"""Closed-box unit tests for all Bag ADT implementations."""

import random
from collections.abc import Hashable, Sequence

import pytest

from paddles.bag import HashTableBag

# Helper functions: can't be named test_... or pytest will call them directly.

BagADT = HashTableBag

pytestmark = [
    pytest.mark.parametrize("Bag", [HashTableBag]),
    pytest.mark.parametrize("items", [
        "", [], (),                         # empty sequences
        "x", [1], (2.0,),                   # sequences of length 1
        "picnic", range(20), [True] * 10    # some/no/all items equal
    ]),
]  # fmt: skip


def check_is_empty(bag: BagADT) -> None:
    """Test that the bag is empty."""
    assert bag.size() == 0
    assert bag.unique() == set()
    assert str(bag) == f"{bag.__class__.__name__}" + "({})"
    assert not bag.has("a")


# Test the creation methods.


def test_init_empty(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803 ARG001
    """Test the creation of empty bags. Ignore the items for this test."""
    check_is_empty(Bag())


def test_init_iterable(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test the creation of bags from an iterable collection."""
    bag = Bag(items)
    for item in set(items):
        assert bag.has(item)
        assert bag.frequency(item) == items.count(item)
    assert bag.size() == len(items)
    assert bag.unique() == set(items)


# Test each modifier method separately.


def test_add_default(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that `add(item)` adds one copy of `item` to the bag."""
    bag = Bag()
    for item in items:
        before = bag.frequency(item)
        bag.add(item)
        assert bag.frequency(item) == before + 1
        assert bag.has(item)
    assert bag.size() == len(items)
    assert bag.unique() == set(items)


def test_add_copies(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that `add(item, copies)` adds `copies` of `item` to the bag."""
    bag = Bag()
    for unique_item in set(items):
        copies = items.count(unique_item)
        bag.add(unique_item, copies)
        assert bag.frequency(unique_item) == copies
        assert bag.has(unique_item)
    assert bag.size() == len(items)
    assert bag.unique() == set(items)


def test_add_preconditions(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that `add(item, copies)` checks the preconditions."""
    bag = Bag()
    for unique_item in set(items):
        with pytest.raises(ValueError, match="must add at least one copy"):
            # test with various non-positive numbers, based on the index
            bag.add(unique_item, -items.index(unique_item))


def test_remove_default(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that `remove(item)` removes one copy of `item` from the bag."""
    bag = Bag(items)
    for item in items:
        before = bag.frequency(item)
        bag.remove(item)
        assert bag.frequency(item) == before - 1
        assert bag.has(item) == (before > 1)
    check_is_empty(bag)


def test_remove_copies(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that `remove(item, copies)` removes `copies` of `item` from the bag."""
    bag = Bag(items)
    for unique_item in set(items):
        copies = items.count(unique_item)
        bag.remove(unique_item, copies)
        assert bag.frequency(unique_item) == 0
        assert not bag.has(unique_item)
    check_is_empty(bag)


def test_remove_preconditions(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that `remove(item, copies)` checks the preconditions."""
    bag = Bag(items)
    for unique_item in set(items):
        with pytest.raises(ValueError):  # noqa: PT011
            # test with various non-positive numbers, based on the index
            bag.remove(unique_item, -items.index(unique_item))
        with pytest.raises(ValueError):  # noqa: PT011
            bag.remove(unique_item, bag.frequency(unique_item) + 1)


def test_union(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that the union of two bags."""
    # create two bags with 1/3 unique and 2/3 common items
    size = len(items)
    items1 = items[size // 3 :]
    items2 = items[: 2 * size // 3]
    bag1 = Bag(items1)
    bag2 = Bag(items2)
    union = bag1.union(bag2)
    for item in set(items):
        assert union.has(item)
        assert union.frequency(item) == max(items1.count(item), items2.count(item))
    assert union.unique() == set(items)
    assert bag1.included_in(union)
    assert bag2.included_in(union)


def test_union_subset(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that the union of a bag with a subset of it is the bag."""
    whole = Bag(items)
    for n in range(len(items) + 1):
        subset = Bag(random.sample(items, n))  # choose n random sequence members
        assert subset.included_in(whole)
        union = whole.union(subset)
        assert union.equal_to(whole)
        union = subset.union(whole)  # check that union is commutative
        assert union.equal_to(whole)


def test_intersection(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test the intersection of two bags."""
    # create two bags with 1/3 unique and 2/3 common items
    size = len(items)
    items1 = items[size // 3 :]
    items2 = items[: 2 * size // 3]
    bag1 = Bag(items1)
    bag2 = Bag(items2)
    common = bag1.intersection(bag2)
    for item in set(items):
        assert common.has(item) == (item in items1 and item in items2)
        assert common.frequency(item) == min(items1.count(item), items2.count(item))
    assert common.unique() == set(items1) & set(items2)
    assert common.included_in(bag1)
    assert common.included_in(bag2)


def test_intersection_subset(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that the intersection of a bag with a subset of it is the subset."""
    whole = Bag(items)
    for n in range(len(items) + 1):
        subset = Bag(random.sample(items, n))  # choose n random sequence members
        assert subset.included_in(whole)
        common = whole.intersection(subset)
        assert common.equal_to(subset)
        common = subset.intersection(whole)  # check that intersection is commutative
        assert common.equal_to(subset)


def test_difference(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test the difference of two bags."""
    # create two bags with at least 1/3 common items
    size = len(items)
    items1 = items[size // 3 :]
    items2 = items[: 2 * size // 3]
    bag1 = Bag(items1)
    bag2 = Bag(items2)
    diff = bag1.difference(bag2)
    for item in set(items):
        assert diff.has(item) == (items1.count(item) > items2.count(item))
        assert diff.frequency(item) == max(items1.count(item) - items2.count(item), 0)
    assert diff.included_in(bag1)


def test_difference_subset(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test the difference between a bag and a subset of it."""
    whole = Bag(items)
    for n in range(len(items) + 1):
        some = random.sample(items, n)  # choose n random sequence members
        subset = Bag(some)
        assert subset.included_in(whole)
        diff = whole.difference(subset)
        for item in set(items):
            assert diff.has(item) == (items.count(item) > some.count(item))
            assert diff.frequency(item) == max(items.count(item) - some.count(item), 0)
        assert diff.size() == len(items) - n
        diff = subset.difference(whole)  # check that difference is not commutative
        check_is_empty(diff)


def test_included_in(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that any subset of a bag is included in it."""
    bag1 = Bag(items)
    bag2 = Bag(items[::-1])
    assert bag1.included_in(bag2)
    assert bag2.included_in(bag1)
    for n in range(len(items)):
        subset = Bag(random.sample(items, n))  # choose n random sequence members
        assert subset.included_in(bag1)
        assert not bag1.included_in(subset)
        assert subset.included_in(bag2)
        assert not bag2.included_in(subset)


def test_equal_to(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that two bags are equal if they contain the same items."""
    bag1 = Bag(items)
    bag2 = Bag(items[::-1])
    assert bag1.equal_to(bag2)
    assert bag2.equal_to(bag1)  # check that equality is commutative
    for n in range(len(items)):
        subset = Bag(random.sample(items, n))
        assert not bag1.equal_to(subset)
        assert not subset.equal_to(bag1)
