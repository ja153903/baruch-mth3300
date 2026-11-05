---
title: "L22: How data is represented"
marimo-version: "0.25.2"
---

# L22: How data is represented

**By the end of this lecture you can:**

- convert between binary, decimal, and hexadecimal
- explain why Python's `int` never overflows, and what happens in languages where it does
- explain why `0.1 + 0.2 != 0.3`, and predict other float surprises
- use `Decimal` (or integer cents) for money
- explain how text becomes numbers and then bytes, with Unicode and UTF-8

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup

**Predict** all three before you run:

```python {.marimo}
print(2**100)
print(0.1 + 0.2 == 0.3)
print(len("café"), len("café".encode("utf-8")))
```

Every surprise here comes from one fact: **a computer stores everything as bits**, and each type has its own rules for turning bits into values.

## 1. Binary: place value in base 2

In base 10, `1011` means 1·1000 + 0·100 + 1·10 + 1·1. In base 2, each place is a power of **2** instead:

| place | 8 | 4 | 2 | 1 |
|---|---|---|---|---|
| bit | 1 | 0 | 1 | 1 |

So `1011` in binary is 8 + 2 + 1 = 11.

```python {.marimo}
print(int("1011", 2))
print(bin(11))
print(0b1011)
```

### Converting by hand: repeated division

To find the digits of a number in some base, divide by the base and keep the remainders. Here are the base-10 digits of 3300, last digit first:

```python {.marimo}
def decimal_digits(n: int) -> list[int]:
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    digits.reverse()
    return digits


print(decimal_digits(3300))
```

**Trace it for base 2 by hand:** 13 ÷ 2 = 6 r **1**, 6 ÷ 2 = 3 r **0**, 3 ÷ 2 = 1 r **1**, 1 ÷ 2 = 0 r **1**. Read the remainders bottom-up: `1101`. Check with `bin(13)`.

You'll write the general version, `to_base`, in the exercises.

## 2. How much fits in k bits?

Each extra bit doubles the number of patterns: k bits hold 2ᵏ different values.

```python {.marimo}
for _k in [1, 8, 16, 32, 64]:
    print(f"{_k:>2} bits: {2**_k:>26,} values")
```

8 bits make a **byte**, which holds 0 to 255.

### Hexadecimal: a shorthand for bits

One hex digit (0–9, then a–f) is exactly 4 bits, so two hex digits are one byte. That's why programmers write colors and memory addresses in hex.

```python {.marimo}
print(hex(255), 0xFF, int("ff", 16))
_color = "ff8800"
print(
    "red:",
    int(_color[0:2], 16),
    "green:",
    int(_color[2:4], 16),
    "blue:",
    int(_color[4:6], 16),
)
```

## 3. Integers

### Python's `int` grows as needed

```python {.marimo}
import sys

for _n in [1, 2**64, 2**200]:
    print(f"{_n.bit_length():>3} bits, {sys.getsizeof(_n)} bytes in memory")
```

Python uses more memory for bigger numbers, so an `int` never overflows. Most languages (C, Java, Rust, and the hardware itself) use a **fixed width**, often 32 or 64 bits.

### Fixed width: what overflow looks like

With 8 bits, arithmetic wraps around at 256. We can simulate it with `% 256`. **Predict:**

```python {.marimo}
print((250 + 10) % 256)
print((0 - 1) % 256)
```

### Negative numbers: two's complement

Hardware stores negative numbers by wrapping too. In 8 bits, `-1` is stored as the same bits as 255, `11111111`. Patterns 0–127 mean themselves, and patterns 128–255 mean -128 to -1.

```python {.marimo}
for _n in [5, -1, -128]:
    print(f"{_n:>5} is stored as {_n % 256:>3} = {_n % 256:08b}")
```

**A real bug:** in 2014, *Gangnam Style* was the first YouTube video to pass 2,147,483,647 views, which is 2³¹ − 1, the largest signed 32-bit integer. YouTube had to switch its view counter to 64 bits. **Predict:** what's the largest signed 64-bit integer?

## 4. Floats: scientific notation in base 2

A `float` is 64 bits: a sign, an exponent, and 52 bits of digits. It works like scientific notation (6.02 × 10²³), but in base 2.

`1/3` has no exact decimal form: 0.3333… goes on forever. In the same way, `1/10` has no exact **binary** form. So `0.1` is stored as the nearest float:

```python {.marimo}
print(f"{0.1:.25f}")
print((0.1).as_integer_ratio())
```

### Consequence 1: never compare floats with `==`

```python {.marimo}
import math

print(0.1 + 0.2 == 0.3, math.isclose(0.1 + 0.2, 0.3))
```

### Consequence 2: big plus small loses the small

**Predict** each line:

```python {.marimo}
print(1e16 + 1 == 1e16)
print((1e16 + 1) - 1e16)
print((1e16 - 1e16) + 1)
```

The order of additions changes the answer. (Python's built-in `sum` uses a cleverer algorithm that hides this, but a plain loop with `+=` doesn't.) The gap between neighboring floats grows with their size:

```python {.marimo}
for _x in [1.0, 1e6, 1e16]:
    print(f"gap after {_x:g}: {math.ulp(_x):g}")
```

### Consequence 3: big integers aren't exact as floats

Floats store integers exactly only up to 2⁵³. **Predict:**

```python {.marimo}
print(float(2**53) == float(2**53 + 1))
```

### Consequence 4: floats have special values

```python {.marimo}
_big = sys.float_info.max
print(_big, _big * 10)
_nan = float("inf") - float("inf")
print(_nan, _nan == _nan)
```

`nan` ("not a number") is the only value that isn't equal to itself.

## 5. Aside: money

Rounding errors in money add up and are never acceptable. Two common fixes:

1. **Integer cents:** store `1999`, not `19.99`. Integers are exact.
2. **`Decimal`:** decimal arithmetic in software. Build it from a **string**, because a float has already lost the exact value.

```python {.marimo}
from decimal import Decimal

print(Decimal("0.1") * 3 == Decimal("0.3"))
print(Decimal(0.1))
```

## 6. Text: characters are numbers

**Unicode** gives every character a number, its **code point**. There are more than 150,000 of them.

```python {.marimo}
print(ord("A"), ord("a"), ord("é"), ord("🐍"))
print(chr(65), chr(9731))
```

String comparison and sorting use code points. **Predict:**

```python {.marimo}
print("Z" < "a")
print(sorted(["banana", "Apple", "cherry"]))
```

### Encoding: code points become bytes

To save text to a file or send it over a network, it must become bytes. **UTF-8** uses 1 to 4 bytes per character: plain English takes 1, and an emoji takes 4.

```python {.marimo}
for _ch in ["A", "é", "€", "🐍"]:
    _encoded = _ch.encode("utf-8")
    print(f"{_ch}  code point {ord(_ch):>6}  {len(_encoded)} bytes: {_encoded}")
```

`len` counts code points, not bytes. That's why L15 used `read_text(encoding="utf-8")`: the same bytes mean different text in another encoding.

### Two strings that look the same

```python {.marimo}
_composed = "é"
_combining = "é"
print(_composed, _combining, _composed == _combining, len(_composed), len(_combining))
```

The second is `e` plus a "combining accent" code point. They look identical but aren't equal, which can matter when you compare user input or names in a CSV.

## 7. Summary

| Type | Stored as | Limit | Watch out for |
|---|---|---|---|
| `int` | as many bits as needed | memory | other languages overflow |
| `float` | 64 bits, binary scientific notation | about 16 significant digits | `==`, big + small, money |
| `Decimal` | decimal digits, in software | you choose the precision | slower; build from strings |
| `str` | Unicode code points | none | bytes ≠ characters; look-alikes |

## AI activity: check the claim

Ask an AI: *"How many bytes does the string `naïve café 🐍` take in UTF-8?"* Write down its answer, then check it:

```python {.marimo}
print(len("naïve café 🐍".encode("utf-8")))
```

If it was wrong, ask it to count again, character by character. Can you explain the right answer to a classmate?

## Exercises (40 minutes)

Open `l22_exercises.py` and run `uv run pytest lectures/22-representation` as you go:

| Group | Functions |
|---|---|
| Warmup | `max_unsigned`, `utf8_bytes` |
| Core | `to_base`, `wrap`, `to_signed`, `approx_equal` |
| Fix the AI's code | `total_cents` |
| Stretch | `machine_epsilon`, `utf8_length` |
