# Replace each None with an f-string built from the variables above it.

# Warmup

price = 1234.5
formatted_price = None  # "$1,234.50"

rate = 0.0725
rate_text = None  # "7.25%"

# Core

invoice = 381
invoice_text = None  # "INV-000381": the number padded with zeros to 6 digits

# The ticker left-aligned in 6 characters, a |, then the price right-aligned
# in 10 characters with 2 decimal places.
ticker = "AAPL"
close = 227.5
table_row = None  # "AAPL  |    227.50"

shares = 25
debug_text = None  # "shares=25". Hint: section 4 of the notes

# The change from old to new as a percent of old, with its sign.
old = 80.0
new = 92.0
change_text = None  # "+15.0%"

# Fix the AI's code: an AI wrote this line, and it has a bug. Find it, then fix it.

# The balance with commas and 2 decimal places.
balance = 9876.5
balance_text = f"${balance:,.2}"  # "$9,876.50"

# Stretch

# The title centered in `width` characters, filled with *.
# Hint: a width can come from a variable, inside its own braces: {x:^{width}}
title = "MTH 3300"
width = 20
banner = None  # "******MTH 3300******"

# Hint: the format type e works like f, but in scientific notation.
avogadro = 6.02214076e23
scientific = None  # "6.02e+23"
