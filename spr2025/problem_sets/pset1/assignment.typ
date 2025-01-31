#set text(font: "New Computer Modern", size: 9pt)

#align(
  center,
  block[
    = MTH 3300 Problem Set 1
    == Due date: February 9, 2025 11:59pm
  ],
)

#align(
  center,
  rect(
    block[
      For the first part, please type up your responses and submit it as a PDF.

      For the programming assignment, please follow the following naming convention for your Python files.
      `mth3300_<lastname>_<firstname>_pset1_part<#>.py`

      So for example, the name of my three files for this problem set would be:
      - `mth3300_abbariao_jaime_pset1_part1.py`
      - `mth3300_abbariao_jaime_pset1_part2.py`
      - `mth3300_abbariao_jaime_pset1_part3.py`

      *If you worked with someone for this assignment, please note who on the PDF!*
    ],
  ),
)

= What will the following statements output? (10 points)

+ `-3 ** 3`
+ `0.1 + 0.3 == 0.4`
+ ```python
  name = "Jeff"
  age = 30

  print(name + age)
  ```
+ `-10 % 3`
+ ```python
  condition1 = False
  condition2 = True

  print(condition1 and condition2)
  ```
+ ```python
  age = 0

  print(not age)
  ```
+ ```python
  some_condition = "False"
  explicit_cast_to_bool = bool(some_condition)

  print(not some_condition)
  ```
+ `6.3 // 2`
+ ```python
  x = 10
  y = 20

  print(x < y and y > 15)
  ```
+ ```python
  x = 5
  y = 2

  print((x + y) * 2 == 14)
  ```

= The Local Store goes Digital

The local corner store, run by Mrs. Chen for 30 years, is finally going digital!
She needs your help to build a simple calculator for her store. Let's help her
step by step to modernize her beloved shop.

== Part 1: The Basic Calculator (10 points)

Mrs. Chen wants to start simple. Every morning, customers come in to buy multiple
items of the same product - like 6 apples or 3 loaves of bread. She's tired of
calculating these by hand!

#rect(
  block[
    *Since we haven't gone over decimal formatting yet, don't worry about
    having to output your result with 2 decimal places.*
  ],
)

Your Task:
Create a program that helps Mrs. Chen:
- Enter the price of any item (like \$2.50 for one apple)
- Enter how many of that item the customer wants
- See the total cost right away

For example, if someone wants 6 apples at \$2.50 each, she should see \$15.00 as
the total.

_Example output:_

```text
Enter the price: $2.50
Enter how many you want: 6
Total cost: $15.00
```

== Part 2: Store Promotion Time! (30 points)

Exciting news! Mrs. Chen is running her first store-wide promotion. She wants to
offer a 5% discount on everything and needs to account for the 8% sales tax that
she has to charge.

Your Task:
Help Mrs. Chen create a calculator that:
- Takes the item price and quantity like before
- Automatically applies the 5% discount to everything
- Adds the required 8% sales tax
- Shows a clear breakdown of the original price, discount, tax, and final price

She wants customers to see exactly how much they're saving!

_Example output:_

```text
Enter the price: $2.50
Enter how many you want: 6
Original price: $15.00
Discount: $0.75
Tax: $1.14
Final price: $15.39
```

== Part 3: The Loyalty Program (50 points)

Mrs. Chen's daughter suggested starting a loyalty program with three tiers:
Bronze, Silver, and Gold (represented as levels 1, 2, and 3). The higher the
level, the more customers save! Each level gives an extra 5% discount
(Level 1 = 5%, Level 2 = 10%, Level 3 = 15%). Plus, to keep things organized,
there's a standard \$10 delivery fee for all orders.

Your Task:
Create the ultimate calculator that:
- Takes the item price and quantity
- Asks for the customer's loyalty level (0, 1, 2, or 3)
- Calculates their special loyalty discount
- Adds the delivery fee and sales tax
- Prints a detailed receipt showing every cost and saving

Mrs. Chen wants her customers to feel special and see all their loyalty rewards
clearly laid out on the receipt!


_Example output:_

```text
Enter the price: $2.50
Enter how many you want: 6
Original price: $15.00
Enter your customer loyalty level: 3
Discount: $2.25
Tax: $1.02
Delivery fee: $10.00
Final price: $23.77
```
