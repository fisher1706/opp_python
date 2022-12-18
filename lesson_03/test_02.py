class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def setCoords(self, x, y):
        # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
        if isinstance(x, int) or isinstance(x, float) and isinstance(y, int) or isinstance(y, float):
            self.__x = x
            self.__y = y
        else:
            print('Coords must be number!')

    def getCoords(self):
        return self.__x, self.__y


if __name__ == '__main__':
    pt = Point(5, 10)
    print(pt.__dict__)
    # print(pt.__x)

    pt.setCoords(10, 20)
    print(pt.__dict__)
    print(pt.getCoords())

    pt.setCoords('10', 20)
