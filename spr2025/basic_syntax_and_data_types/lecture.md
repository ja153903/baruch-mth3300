---
title: MTH 3300 Spring 2025
sub_title: Lecture 2
author: Jaime Abbariao
---

# Primitive data types

We'll go over some fundamental data types that exist in Python.

There are going to be more later on, but for now, we'll go over the following:

- `int`
- `float`
- `bool`
- `str`

<!-- end_slide -->

# Variables

Variables exist as a mechanism to store information that we can potentially read or mutate within a computer program

Here are some examples of doing so:

```python
name = "jaime"
ten = 10
not_true = False

sum_of_two_numbers = 1 + 1

name = "john" # we can rename variables as well
```

**Exercise:** Create the following variables and assign any value you want to it

- `first_name`
- `last_name`
- `email`

<!-- end_slide -->

# Variables

## Best practices for naming variables

<!-- end_slide -->

# Variables

## Multiple inline assignments

# Variables

## 

# Type conversion

In Python, there are ways to coerce types to go from one to another. There are going to be times when
you need a string to be an integer or an integer to be a string.

We'll explore this with the primitive types we know.

<!-- end_slide -->

# Type conversion

## int -> str

If we want to convert an integer to a string, one way we can do so is by using the `str` function.

```python
a_number = 42

a_number_as_str = str(a_number) # Output: "42"
```

<!-- end_slide -->

# Type conversion

## float -> str

If we want to convert a float to a string, one way we can do so is by using the `str` function.

```python
a_number = 42.0

a_number_as_str = str(a_number) # Output: "42.0"
```

<!-- end_slide -->

# Type conversion

## bool -> str

If we want to convert a boolean to a string, one way we can do so is by using the `str` function.

```python
a_bool = False

a_bool_as_str = str(a_bool) # Output: "False"
```

<!-- end_slide -->

# Type conversion

## int -> float

If we want to convert an integer to a float, one way we can do so is by using the `float` function.

```python
an_int = 12

an_int_as_float = float(an_int) # Output: 12.0
```

<!-- end_slide -->

# Type conversion

## float -> int

If we want to convert an float to an integer, one way we can do so is by using the `int` function.

```python
a_float = 12.2

a_float_as_int = int(a_float) # Output: 12
```

Notice here that when we cast a float to an int, we lose the precision!

<!-- end_slide -->

# Type conversion

## str | int | float -> bool

If we try to convert any of the primitive types to a boolean, we notice a funny pattern.

```python
# what is the output the following?

bool("")
bool("some_string")

bool(0.0)
bool(12.0)
bool(-0.2)

bool(1)
bool(0)
bool(-1)
bool(100)
```

We say that some values are **truthy** or **falsy** based on their values.

In the above examples, we categorize an empty string `""`, `0`, and `0.0` as falsy.

We can then see that a string with more than character, non-zero integer and floating point values
are considered truthy.

<!-- end_slide -->

# Basic input and output operations

<!-- end_slide -->
