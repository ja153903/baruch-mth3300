---
title: Lecture 3
sub_title: MTH 3300 Spr 2025
author: Jaime Abbariao
---

# Problem set released

Just a reminder that the problem set was released on Friday.

It covers everything up to logical operators.

<!-- end_slide -->

# Recap

## Assignment operators

We talked about a number of operators last class:

- `+`: addition
- `-`: subtraction
- `*`: multiplication
- `/`: division
- `//`: floor division
- `%`: modulo
- `**`: exponentiation

<!-- end_slide -->

# Recap

## Relational operators

- `==`: equals
- `!=`: not equals
- `<`: less than
- `<=`: less than or equal to
- `>`: greater than
- `>=`: greater than or equal to

<!-- end_slide -->

# Recap

## Logical operators

- `and`
- `or`
- `not`

<!-- end_slide -->

# Recap

## **Task 1: Combined Operations**  

Write a Python program that combines arithmetic, relational, and logical operators.  

1. Ask the user to input three numbers, `a`, `b`, and `c`.  
2. Perform the following operations:  
   - Check if `a` is greater than `b` and `b` is greater than `c`.  
   - Check if `a` is equal to `b` or `b` is equal to `c`.  
   - Check if the sum of `a` and `b` is greater than `c`.  
   - Check if `a` is not equal to `c`.  

**Example Output:**  
```text
Enter the first number: 10  
Enter the second number: 5  
Enter the third number: 2  
Is a > b > c? True  
Is a == b or b == c? False  
Is (a + b) > c? True  
Is a != c? True  
```

<!-- end_slide -->

# Recap

## Task 1: Combined Operations

### Solution

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print(f"Is a > b > c? {a > b > c}")
print(f"Is a == b or b == c? {a == b or b == c}")
print(f"Is (a + b) > c? {(a + b) > c}")
print(f"Is a != c? {a != c}")
```

<!-- end_slide -->

# if-elif-else statements

Define conditional statements and why they are important in programming

<!-- end_slide -->

# if-elif-else statements

Give an example by using grading systems

<!-- end_slide -->

# if-elif-else statements

Here's a simple example of an `if` statement in Python:

```python
temperature = int(input("How's the weather today? "))

if temperature > 80:
  print("It's hot today!")
```

<!-- end_slide -->

# if-elif-else statements

Explain the syntax of `if-elif-else` statements

<!-- end_slide -->

# if-elif-else statements

## Exercise

Suppose that we want to build out the logic for converting numerical grades
to letter grades based on Baruch's system. How would we do this?

<!-- end_slide -->

# if-elif-else statements

## Common pitfalls

### Incorrect Indentation

Python relies on indentation to define code blocks. Incorrect indentation can lead to syntax errors or logical errors.

```python
if x > 10:
print("x is greater than 10")
else:
  print("x is 10 or less")
```

The above snippet will return an `IndentationError`. To fix this, you must properly indent the line under the condition

```python
if x > 10:
  print("x is greater than 10")
else:
  print("x is 10 or less")
```
<!-- end_slide -->

# if-elif-else statements

## Common pitfalls

### Misusing = instead of ==

Using `=` (the assignment operator) instead of `==` (equality operator) is a common mistake.

```python
x = 5

if x = 10:
  print("x is 10")
```

This will give you a `SyntaxError`! To fix this, we should use the equality operator

```python
x = 5

if x == 10:
  print("x is 10")
```

<!-- end_slide -->

# if-elif-else statements

## Common pitfalls

### Overlapping conditions

When conditions `if` and `elif` statements overlap, the first condition will execute, and the rest will be ignored.
This can lead to unexpected behavior.

```python
score = 85

if score >= 60:
  print("Pass")
elif score >= 85: # This condition will never be checked!
  print("Good job!")
```

In order to fix this, we need to make sure we check the **most specific** condition first:

```python
score = 85

if score >= 85:
  print("Good job!")
elif score >= 60: # This condition will never be checked!
  print("Pass")
```

<!-- end_slide -->

# if-elif-else statements

## Exercise

Write a program that asks the user for their age and prints whether they are a child, teenager, adult, or senior.

For this example, we can assume that senior citizens are anyone over the age of 65.

<!-- end_slide -->

# if-elif-else statements

## Solution

```python
age = int(input("How old are you? "))

if age < 13:
  print("child")
elif age < 20:
  print("teenager")
elif age < 65:
  print("adult")
else:
  print("senior")
```

<!-- end_slide -->

# Lab time

- Write a program that asks the user for a number and determine if that number is even or odd.

```text
What is your number? 2
2 is even
```

- Write a program that asks a user's BMI and categorizes it as underweight, normal, overweight, or obese.
  - under 18.5 is underweight
  - 18.5 to 24.9 is normal
  - 25.0 to 29.9 is overweight
  - over 30 is obese

<!-- end_slide -->

# Lab time

## Solution

```python
num = int(input("What is your number? "))
if num % 2 == 0:
  print(f"{num} is even")
```

<!-- end_slide -->

# Lab time

## Solution

```python
bmi = float(input("What is your BMI? "))
if bmi < 18.5:
  print("You are underweight")
elif 18.5 <= bmi < 25:
  print("You are normal")
elif 25 <= bmi < 30:
  print("You are overweight")
else:
  print("You are obese")
```
