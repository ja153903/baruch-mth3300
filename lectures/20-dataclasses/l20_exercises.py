from dataclasses import dataclass


@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError

    def scale(self, factor: float) -> None:
        """Multiply both sides by factor, changing this rectangle."""
        raise NotImplementedError
