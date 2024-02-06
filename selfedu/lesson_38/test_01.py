from dataclasses import dataclass, field
from pprint import pprint


class Thing:
    def __init__(self, name, weight, price, dims=[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    def __repr__(self):
        return f"Thing: {self.__dict__}"


@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)

    def __eq__(self, other):
        return self.weight == other.weight


"""
__init()__, __repr__, __eq__
"""

if __name__ == '__main__':
    t_1 = Thing("book", 100, 1024)
    print(t_1)

    t_1.dims.append(10)
    print(t_1)
    print("*" * 200)

    t_2 = Thing("book", 100, 1024)
    print(t_2)
    print("*" * 200)

    td_1 = ThingData("book", 100, 1024)
    print(td_1)

    td_2 = ThingData("book", 100, 1024)
    print(td_1 == td_2)
    print("*" * 200)

    td_2.dims.append(10)

    td_3 = ThingData("zapel", 1000)
    print(td_3.__dict__)

    # pprint(ThingData.__dict__)
