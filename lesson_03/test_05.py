class Point:
    WIDTH = 5
    __slots__ = ['__x', '__y']

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        else:
            return False

    def setCoords(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print('Coords must be number!')

    def getCoords(self):
        return self.__x, self.__y


if __name__ == '__main__':
    pt = Point(5, 10)
    pt.z = 1



