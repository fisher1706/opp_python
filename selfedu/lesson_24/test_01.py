class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"__init__ from GEOM for {self.__class__}")
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill="red"):
        super().__init__(x1, y1, x2, y2)
        print(f"__init__ from REACT for {self.__class__}")
        self.__fill = fill

    @staticmethod
    def draw():
        print("draw React")


if __name__ == '__main__':
    react = Rect(1, 2, 3, 4)
    print(react.__dict__)

    print(react.get_coords())

    print(react._Rect__fill)
    print(react._Geom__x1)
