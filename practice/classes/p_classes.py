from dataclasses import dataclass, field


@dataclass
class Stack:
    items: list[int] = field(default_factory=list)

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        """Remove and return the top item. Raise IndexError if the stack is empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError


@dataclass
class Inventory:
    stock: dict[str, int] = field(default_factory=dict)

    def add(self, item: str, qty: int) -> None:
        raise NotImplementedError

    def remove(self, item: str, qty: int) -> None:
        """Raise ValueError if there isn't enough stock; in that case, change nothing."""
        raise NotImplementedError

    def count(self, item: str) -> int:
        raise NotImplementedError
