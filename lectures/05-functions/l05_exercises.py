# Warmup


def cube(x):
    """Return x to the third power."""
    raise NotImplementedError


def average(a, b, c):
    """Return the average of three numbers."""
    raise NotImplementedError


# Core


def sales_tax(price, rate=0.08875):
    """The tax on price, rounded to cents.

    The rate is New York City's unless you give another one:
    sales_tax(24.99) == 2.22 and sales_tax(50, rate=0.1) == 5.0
    """
    raise NotImplementedError


def name_tag(first, last):
    """The last name in capitals, a comma and a space, then the first name capitalized.

    name_tag("ada", "lovelace") == "LOVELACE, Ada"
    """
    raise NotImplementedError


def distance(x1, y1, x2, y2):
    """The straight-line distance between the points (x1, y1) and (x2, y2).

    distance(0, 0, 3, 4) == 5.0.
    Add `import math` at the top of this file, and use math.sqrt.
    """
    raise NotImplementedError


def shares_affordable(cash, price):
    """How many whole shares at `price` you can buy with `cash`. Return an int.

    shares_affordable(1000, 37.5) == 26
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def rent_share(rent, people):
    """Each person's share of the rent, rounded to cents."""
    print(round(rent / people, 2))


# Stretch


def leftover_cash(cash, price):
    """The cash left after you buy as many whole shares as you can.

    Call shares_affordable. leftover_cash(1000, 37.5) == 25.0
    """
    raise NotImplementedError


def doubling_time(rate):
    """The exact number of years for money to double at `rate` a year.

    The formula is log(2) / log(1 + rate). Use math.log. Then compare your
    answer with the rule of 72, which says 72 / (rate * 100).
    """
    raise NotImplementedError
