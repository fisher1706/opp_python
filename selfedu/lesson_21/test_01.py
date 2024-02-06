class Geom:
    name = "Geom"

    def __init__(self):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    @staticmethod
    def draw():
        print("draw geom")


class Line(Geom):
    name = "Line"

    @staticmethod
    def draw():
        print("draw line")


class React(Geom):
    @staticmethod
    def draw():
        print("draw React")


if __name__ == '__main__':
    line = Line()
    rect = React()

    line.set_coords(1, 1, 2, 2)
    rect.set_coords(1, 1, 2, 2)

    print(line.__dict__)
    print(rect.__dict__)

    print(line.name)
    print(rect.name)
