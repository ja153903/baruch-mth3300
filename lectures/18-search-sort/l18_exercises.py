# Warmup


def count_occurrences(xs: list[int], target: int) -> int:
    """Count with a linear scan. Don't use .count()."""
    raise NotImplementedError


def last_index(xs: list[int], target: int) -> int:
    """The index of the last copy of target in xs, or -1 if it isn't there.

    last_index([4, 2, 4, 1], 4) == 2. Don't use .index().
    """
    raise NotImplementedError


# Core


def insertion_sort(xs: list[int]) -> list[int]:
    """Return a new sorted list using insertion sort. Don't use sorted() or .sort()."""
    raise NotImplementedError


def sort_by_value(holdings: dict[str, float]) -> list[str]:
    """The tickers, from the largest holding to the smallest. Break ties alphabetically.

    Use sorted with a key.
    """
    raise NotImplementedError


def count_inversions(xs: list[int]) -> int:
    """How many pairs of positions i < j have xs[i] > xs[j].

    A sorted list has 0 inversions. count_inversions([3, 1, 2]) == 2.
    """
    raise NotImplementedError


def closest(xs: list[int], target: int) -> int:
    """The value in the sorted list xs that's closest to target. If two tie, the smaller one.

    xs is not empty. Use bisect.bisect_left, then compare the values on either side.
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def bubble_sort(xs: list[int]) -> list[int]:
    """A new sorted list, using bubble sort. Don't change xs.

    Bubble sort sweeps through the list, swapping neighbors that are out of order.
    After each sweep, the largest value that's left has "bubbled" to the end.
    """
    result = xs.copy()
    for i in range(len(result)):
        for j in range(len(result) - i - 2):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


# Stretch


def two_sum_sorted(xs: list[int], target: int) -> bool:
    """True if the values at two different positions in the sorted list xs add up to target.

    Do it in one pass: start one index at each end, and move them toward each other.
    """
    raise NotImplementedError
