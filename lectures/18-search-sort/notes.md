---
title: "L18: Searching and sorting"
marimo-version: "0.25.2"
---

# L18: Searching and sorting

**By the end of this lecture you can:**

- implement linear search and binary search
- implement a simple sort, and describe how merge sort works
- explain why sorted data makes searching faster

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Linear search

Check every element in turn. It works on any list.

```python {.marimo}
def linear_search(xs: list[int], target: int) -> int:
    for i, x in enumerate(xs):
        if x == target:
            return i
    return -1


print(linear_search([7, 3, 9, 1], 9), linear_search([7, 3, 9, 1], 4))
```

## 2. Binary search

This needs a **sorted** list. Each step throws away half of what's left, like looking up a word in a dictionary.

```python {.marimo}
def binary_search_steps(xs: list[int], target: int) -> int:
    lo, hi, steps = 0, len(xs) - 1, 0
    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2
        if xs[mid] == target:
            break
        if xs[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return steps


million = list(range(1_000_000))
print("binary search steps for 1,000,000 items:", binary_search_steps(million, 765_432))
```

**Predict:** about how many steps would a linear search need for the same target?

## 3. Selection sort

Repeatedly find the smallest remaining element and move it to the front.

```python {.marimo}
def selection_sort(xs: list[int]) -> list[int]:
    result = xs.copy()
    for i in range(len(result)):
        smallest = min(range(i, len(result)), key=lambda j: result[j])
        result[i], result[smallest] = result[smallest], result[i]
    return result


print(selection_sort([5, 2, 9, 1, 5, 6]))
```

## 4. Merge sort: the idea

1. Split the list in half.
2. Sort each half (recursively).
3. **Merge** the two sorted halves, by repeatedly taking the smaller front element.

You'll build it in homework 10.

## 5. In practice

```python {.marimo}
people = [("Ada", 36), ("Alan", 41), ("Grace", 85)]
print(sorted(people, key=lambda p: p[1], reverse=True))
```

Python's built-in `sorted` uses **Timsort**, a hybrid of merge sort and insertion sort. Use it in real code. Write your own sorts only to learn how they work.

## AI activity

Ask an AI to visualize binary search on `[1, 3, 5, 7, 9, 11, 13]` for target `11`, step by step. Check each step against `binary_search_steps`.

**Exercises:** `l18_exercises.py`
