class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"__init__ from GEOM for {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    @staticmethod
    def draw():
        print("draw line")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        print(f"__init__ from REACT for {self.__class__}")
        self.fill = fill

    @staticmethod
    def draw():
        print("draw React")


if __name__ == '__main__':
    line = Line(0, 0, 10, 20)
    print(line.__dict__)

    react = Rect(1, 2, 3, 4)
    print(react.__dict__)
