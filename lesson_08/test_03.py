class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Styles:
    def __init__(self):
        print('constructor styles')
        super().__init__()


class Pos:
    def __init__(self):
        print('constructor pos')
        super().__init__()


class LineOne(Pos, Styles):
    def __init__(self, sp: Point, ep: Point, color='red', width=1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width
        super().__init__()

    def draw(self):
        print(f'Draw line one: {self._sp}, {self._ep}, {self._color}, {self._width}')


class LineTwo(Styles, Pos):
    def __init__(self, sp: Point, ep: Point, color='red', width=1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width
        super().__init__()

    def draw(self):
        print(f'Draw line two: {self._sp}, {self._ep}, {self._color}, {self._width}')


if __name__ == '__main__':
    l1 = LineOne(Point(1, 2), Point(10, 20), 'green', 5)
    l1.draw()

    l2 = LineTwo(Point(10, 20), Point(100, 200), 'red', 5)
    l2.draw()

    print(LineOne.__mro__)
    print(LineTwo.__mro__)
