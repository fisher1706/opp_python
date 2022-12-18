class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Styles:
    def __init__(self, color='red', width=1):
        print('constructor styles')
        self._color = color
        self._width = width


class Pos:
    def __init__(self, sp: Point, ep: Point, *args):
        print('constructor pos')
        self._sp = sp
        self._ep = ep
        Styles.__init__(self, *args)


class Line(Pos, Styles):
    def draw(self):
        print(f'Draw line: {self._sp}, {self._ep}, {self._color}, {self._width}')


if __name__ == '__main__':
    l = Line(Point(1, 2), Point(10, 20), 'green', 5)
    l.draw()
