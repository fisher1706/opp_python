class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Line:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def drawLine(self):
        print(f'Draw line: {self._sp}, {self._ep}, {self._color}, {self._width}')


class Rect:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def drawLine(self):
        print(f'Draw rect: {self._sp}, {self._ep}, {self._color}, {self._width}')


if __name__ == '__main__':
    print(issubclass(Point, object))
    l = Line(Point(1, 2), Point(10, 20))
    l.drawLine()

    r = Rect(Point(30, 40), Point(70, 80))
    r.drawLine()
