from dataclasses import dataclass
from typing import Any


@dataclass
class Goods:
    uid: Any
    price: Any = None
    weight: Any = None


@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    price: float = 0
    weight: int | float = 0


if __name__ == '__main__':
    b1 = Book(1)
    print(b1)

    b2 = Book(1, 1000, 100, "python", "zapel")
    print(b2)
