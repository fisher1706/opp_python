class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __setCoordX(self, x):
        print('call __setCoordsX')
        self.__x = x

    def __getCoordX(self):
        print('call __getCoordX')
        return self.__x

    coordX = property(__getCoordX, __setCoordX)


if __name__ == '__main__':
    pt = Point(1, 2)
    pt.coordX = 100
    x = pt.coordX
    print(x)




