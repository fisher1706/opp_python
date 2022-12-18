class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def __setCoordX(self, x):
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError('Incorrect format data')

    def __getCoordX(self):
        return self.__x

    def __delCoordX(self):
        print('Delete property')
        del self.__x

    coordX = property(__getCoordX, __setCoordX, __delCoordX)


if __name__ == '__main__':
    pt = Point(1, 2)
    pt.coordX = 100
    x = pt.coordX
    print(x)

    del pt.coordX
    




