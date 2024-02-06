class B1:
    pass


class B2:
    pass


def method_1(self):
    print(self.__dict__)


A = type(
    "Point",
    (B1, B2),
    {
        "MAX_COORD": 100,
        "MIN_COORD": 0,
        "method1": method_1,
        "method2": lambda self: print(self.MAX_COORD)
    }
)


"""
A = type("Point", (), {"MAX_COORD": 100, "MIN_COORD": 0})
            equal:
class A:
    MAX_COORD = 100
    MIN_COORD = 0  
"""

if __name__ == '__main__':
    pt = A()

    print(pt.MAX_COORD)
    print("*" * 200)

    print(A.__mro__)
    print("*" * 200)

    pt.method1()
    print("*" * 200)

    pt.method2()
