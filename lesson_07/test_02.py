class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'

    def isDigit(self):
        if (isinstance(self.__x, int) or isinstance(self.__x, float)) and\
                (isinstance(self.__y, int) or isinstance(self.__y, float)):
            return True
        else:
            return False

    def isInt(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        else:
            return False


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def setCoords(self, sp, ep):
        if sp.isDigit() and ep.isDigit():
            self._sp = sp
            self._ep = ep
        else:
            print('Coords must be digit')


class Line(Prop):
    def drawLine(self):
        print(f'Draw line: {self._sp}, {self._ep}, {self._color}, {self._width}')

    def setCoords(self, sp: Point, ep: Point = None):
        if ep is None:
            if sp.isInt():
                self._sp = sp
            else:
                print('Coords must be int')
        else:
            if sp.isInt() and ep.isInt():
                Prop.setCoords(self, sp, ep)
            else:
                print('Coords must be int')


if __name__ == '__main__':
    l = Line(Point(1, 2), Point(10, 20))
    l.drawLine()

    l.setCoords(Point(10, 20), Point(100, 200))
    l.drawLine()

    l.setCoords(Point(-10, -20))
    l.drawLine()
