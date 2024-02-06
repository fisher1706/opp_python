class Geom:
    __name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"__init__ from GEOM for {self.__class__}")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill="red"):
        super().__init__(x1, y1, x2, y2)
        print(f"__init__ from REACT for {self.__class__}")
        self._fill = fill

    @staticmethod
    def draw():
        print("draw React")

    def get_coords(self):
        return self._x1, self._y1, self._x2, self._y2


if __name__ == '__main__':
    rect = Rect(1, 2, 3, 4)
    print(rect.__dict__)

    print(rect.get_coords())
    print(rect._x1)
