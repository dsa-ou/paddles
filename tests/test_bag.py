"""Closed-box unit tests for all Bag ADT implementations."""

from collections.abc import Hashable, Sequence

import pytest

from paddles import HashTableBag

# Helper functions: can't be named test_... or pytest will call them directly.

BagADT = HashTableBag

pytestmark = [
    pytest.mark.parametrize("Bag", [HashTableBag]),
    pytest.mark.parametrize("items", ["picnic", range(20), [True] * 10]),
]


def check_is_empty(bag: BagADT) -> None:
    """Test that the bag is empty."""
    assert bag.size() == 0
    with pytest.raises(ValueError, match="can't remove more copies than the bag has"):
        bag.remove("a")
    assert str(bag) == f"{bag.__class__.__name__}" + "({})"


# Test the creation methods.


def test_init_empty(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803 ARG001
    """Test the creation of empty bags. Ignore the items for this test."""
    check_is_empty(Bag())


def test_init_iterable(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test the creation of bags from an iterable collection."""
    bag = Bag(items)
    assert bag.size() == len(items)
    for item in items:
        assert bag.frequency(item) == items.count(item)


# Test each modifier method separately.


def test_add(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that `add(item)` adds `item` to the bag."""
    bag = Bag()
    for item in items:
        before = bag.frequency(item)
        bag.add(item)
        assert bag.frequency(item) == before + 1
        assert bag.has(item)
    assert bag.size() == len(items)


def test_remove(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that `remove(item)` removes `item` from the bag."""
    bag = Bag(items)
    for item in items:
        before = bag.frequency(item)
        bag.remove(item)
        assert bag.frequency(item) == before - 1
        assert bag.has(item) == (before > 1)
    assert bag.size() == 0


def test_add_copies(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that `add(item, copies)` adds `copies` of `item` to the bag."""
    bag = Bag()
    for item in set(items):
        copies = items.count(item)
        bag.add(item, copies)
        assert bag.frequency(item) == copies
        assert bag.has(item)
    assert bag.size() == len(items)
    assert bag.unique() == set(items)


def test_remove_copies(Bag: type[BagADT], items: Sequence[Hashable]) -> None:  # noqa: N803
    """Test that `remove(item, copies)` removes `copies` of `item` from the bag."""
    bag = Bag(items)
    for unique in set(items):
        copies = items.count(unique)
        bag.remove(unique, copies)
        assert bag.frequency(unique) == 0
        assert not bag.has(unique)
    assert bag.size() == 0
