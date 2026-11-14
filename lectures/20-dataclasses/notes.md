---
title: "L20: Classes and objects"
marimo-version: "0.25.2"
---

# L20: Classes and objects

**By the end of this lecture you can:**

- write a class by hand with `__init__`, methods that use `self`, and `__repr__`
- keep an object's data valid by changing it only through methods
- use `@dataclass` to skip the boilerplate when a class is mostly data
- make frozen objects and change them with `copy.replace`
- read a subclass that uses `super()` and `@override`

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Why classes?

A tuple like `("AAPL", 10)` doesn't say what each value means, and nothing stops you from setting the shares to `-500`. A **class** bundles data with the functions allowed to change it.

```python {.marimo}
class Position:
    def __init__(self, ticker: str, shares: int = 0) -> None:
        self.ticker = ticker
        self.shares = shares

    def buy(self, shares: int) -> None:
        self.shares += shares

    def sell(self, shares: int) -> None:
        if shares > self.shares:
            raise ValueError(f"can't sell {shares}, only have {self.shares}")
        self.shares -= shares

    def value(self, price: float) -> float:
        return self.shares * price

    def __repr__(self) -> str:
        return f"Position('{self.ticker}', {self.shares})"


_pos = Position("AAPL")
_pos.buy(10)
_pos.sell(3)
print(_pos, _pos.value(190.5))
```

- `Position("AAPL")` creates a new object and calls `__init__` to set it up. `self` is that new object.
- `self.ticker = ticker` creates an **attribute**: a variable that belongs to this one object.
- `_pos.buy(10)` is shorthand for `Position.buy(_pos, 10)`. Whatever is before the dot becomes `self`.
- `__repr__` is what `print` and the REPL show. Without it you'd see `<Position object at 0x10a3f...>`. Names with double underscores ("dunder" methods) are methods Python calls for you.

## 2. An object guards its own data

```python {.marimo}
_pos = Position("MSFT", 5)
try:
    _pos.sell(8)
except ValueError as err:
    print("rejected:", err)
print(_pos)
```

The rule "you can't sell what you don't own" lives in one place, `sell`. As long as every change goes through a method, no `Position` can break it.

**Predict:** what does this print?

```python {.marimo}
_a = Position("NVDA", 2)
_b = _a
_b.buy(1)
print(_a, _a is _b, _a == Position("NVDA", 3))
```

`_b = _a` doesn't copy anything. Both names point to one object, just like lists in L11. And `==` returns `False`: a class without its own `__eq__` only counts an object as equal to itself.

## 3. `@dataclass` writes the boilerplate

Many classes are mostly data. Writing `__init__`, `__repr__`, and `__eq__` for them by hand is repetitive, so `@dataclass` writes all three from the list of fields.

```python {.marimo}
from dataclasses import dataclass, field


@dataclass
class Trade:
    ticker: str
    shares: int
    price: float

    def cost(self) -> float:
        return self.shares * self.price


_t = Trade("AAPL", 10, 190.5)
print(_t, _t.cost(), _t == Trade("AAPL", 10, 190.5))
```

Dataclasses can have methods too, and they can hold other objects:

```python {.marimo}
@dataclass
class Portfolio:
    trades: list[Trade] = field(default_factory=list)

    def add(self, trade: Trade) -> None:
        self.trades.append(trade)

    def total_cost(self) -> float:
        return sum(t.cost() for t in self.trades)


book = Portfolio()
book.add(Trade("AAPL", 10, 190.5))
book.add(Trade("MSFT", 5, 410.25))
print(f"{book.total_cost():,.2f}")
```

**Predict:** why `field(default_factory=list)` instead of `= []`? (Hint: aliasing, L11.)

| Use | When |
|---|---|
| `@dataclass` | The class is mostly fields: a trade, a point, a row from a CSV file |
| A hand-written class | `__init__` needs to do real work, or you want full control over every method |

## 4. Frozen dataclasses and `copy.replace`

```python {.marimo}
import copy


@dataclass(frozen=True)
class Quote:
    ticker: str
    price: float

    def change_from(self, earlier: Quote) -> float:
        """Percent change since an earlier quote."""
        return (self.price - earlier.price) / earlier.price * 100


monday = Quote("AAPL", 190.0)
tuesday = copy.replace(monday, price=195.7)
print(monday, tuesday, f"{tuesday.change_from(monday):.1f}%")
```

A frozen object can't change after it's created: `monday.price = 1` raises `FrozenInstanceError`. To "change" one, `copy.replace` (Python 3.13) makes a new object with some fields swapped. Frozen objects can be dict keys and set members.

Notice that `earlier: Quote` refers to the class *inside its own body*. Since Python 3.14, annotations are evaluated lazily, so this just works.

## 5. A light look at inheritance

A **subclass** starts with everything its parent class has, and replaces the parts that differ.

```python {.marimo}
from typing import override


class ShortablePosition(Position):
    """A position that may go negative (a short sale), down to a limit."""

    def __init__(self, ticker: str, max_short: int) -> None:
        super().__init__(ticker)
        self.max_short = max_short

    @override
    def sell(self, shares: int) -> None:
        if self.shares - shares < -self.max_short:
            raise ValueError(f"short limit is {self.max_short}")
        self.shares -= shares


_s = ShortablePosition("TSLA", max_short=5)
_s.sell(3)
print(_s, _s.value(250.0), isinstance(_s, Position))
```

- `class ShortablePosition(Position)` inherits `buy`, `value`, and `__repr__`. That's why it prints as `Position(...)`.
- `super().__init__(ticker)` runs the parent's setup, and then the subclass adds its own attribute.
- `@override` says "this replaces a parent method." If you misspell it as `def sel(...)`, ty reports an error instead of silently adding a new method.
- Any code written for a `Position` also works with a `ShortablePosition`.

That's as far as this course goes. Python code uses inheritance much less than Java does. Most of the time, small classes and dataclasses are all you need.

## AI activity: give your AI a tool

So far your AI could only read and write text. With **MCP** (Model Context Protocol) you can give it tools: Python functions it calls to get exact answers. Every coding AI in this course supports MCP, so one server works in all of them.

An MCP tool is an ordinary function. The AI learns how to call it from three things you already write: the function name, the **type hints**, and the **docstring**.

```python {.marimo}
from mcp.server.mcpserver import MCPServer


@dataclass
class Holding:
    ticker: str
    shares: int
    price: float
    value: float


server = MCPServer("portfolio")


@server.tool()
def value_holding(ticker: str, shares: int, price: float) -> Holding:
    """Value a stock holding: shares times price per share."""
    return Holding(ticker.upper(), shares, price, shares * price)


print(value_holding("aapl", 10, 190.5))  # still a normal function you can test
_tool = (await server.list_tools())[0]
_tool.input_schema  # what the AI sees: built from your type hints
```

The AI can't pass `"ten"` for `shares`: the type hint `int` is enforced before your code runs.

**Try it with a real agent:**

1. Save a server like the one above as `mcp_server.py` at the top of your course folder, ending with:

   ```python
   if __name__ == "__main__":
       server.run()
   ```

2. Tell each tool where your server is. They use different files for the same information:

   `.mcp.json`, for Copilot (and Claude Code):

   ```json
   {
     "mcpServers": {
       "portfolio": {"type": "stdio", "command": "uv", "args": ["run", "python", "mcp_server.py"]}
     }
   }
   ```

   `opencode.jsonc`, for OpenCode:

   ```jsonc
   {
     "mcp": {
       "servers": {
         "portfolio": {"type": "local", "command": ["uv", "run", "python", "mcp_server.py"]}
       }
     }
   }
   ```

   If Copilot doesn't list your server under its tools, open the command palette, run **MCP: Add Server**, choose **Command (stdio)**, and enter `uv run python mcp_server.py`.

3. In Copilot's **Agent** mode, ask: *"What are 37 shares of MSFT worth at 412.17?"* Check that it called `value_holding` instead of doing the arithmetic itself. Ask the same thing in OpenCode.
4. Write a pytest test for `value_holding`. You test MCP tools the same way as any function.

## Exercises (40 minutes)

Open `l20_exercises.py` and run `uv run pytest lectures/20-dataclasses` as you go. Do them in order:

| Group | Classes |
|---|---|
| Warmup | `Tally`, `Rectangle` |
| Core | `Bond`, `Gradebook`, `CurvedGradebook`, `Cart` |
| Fix the AI's code | `Watchlist` |
| Stretch | `Money` |
