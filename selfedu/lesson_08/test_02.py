class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        print("__getattribute__: " + item)
        if item == "x":
            raise ValueError("access denied")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print(f"__setattr__: key - {key}, value - {value}")
        if key == "z":
            raise AttributeError("invalid attr name")
        else:
            object.__setattr__(self, key, value)
            """
            or
            """
            # self.__dict__[key] = value
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print(f"__getattr__: {item}")
        return False

    def __delattr__(self, item):
        print(f"__delattr__: {item}")
        object.__delattr__(self, item)


if __name__ == '__main__':
    pt1 = Point(1, 2)
    print(pt1.y)

    """
    can not get "x"
    """
    # print(pt1.x)

    """
    can not create "z"
    """
    # pt1.z = 5

    """
    __getattr__
    """
    print(pt1.pp)
    print(pt1.MAX_COORD)

    """
    __delattr__
    """
    del pt1.x

    print(pt1.__dict__)
    print(dir(pt1))
