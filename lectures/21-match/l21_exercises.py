def describe(value: object) -> str:
    """Use match:
    - an empty list           -> "empty"
    - a list of one element   -> "one item"
    - any other list          -> "many items"
    - a 2-tuple (x, y)        -> "point at x, y", for example "point at 3, 4"
    - anything else           -> "unknown"
    """
    raise NotImplementedError


def calculate(expr: tuple) -> float:
    """expr is ("add", a, b), ("mul", a, b), or ("neg", a). Raise ValueError otherwise."""
    raise NotImplementedError
