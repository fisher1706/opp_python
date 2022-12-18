class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        print('constructor base class')
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def getWidth(self):
        return self.__width


class Line(Prop):
    def __init__(self, *args):
        print('overridden constructor Line')
        # Prop.__init__(self, *args)
        super().__init__(*args)
        self.__width = 5

    def drawLine(self):
        print(f'Draw line: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}')


class Rect(Prop):
    def drawLine(self):
        print(f'Draw rect: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}')


if __name__ == '__main__':
    print(issubclass(Point, object))
    l = Line(Point(1, 2), Point(10, 20))
    print(l.__dict__)
    l.drawLine()

    r = Rect(Point(30, 40), Point(70, 80))
    r.drawLine()
