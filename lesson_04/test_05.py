class CoordValue:
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Point:
    coordX = CoordValue('coordX')
    coordY = CoordValue('coordY')

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


if __name__ == '__main__':
    pt = Point(1, 2)
    pt.coordX = 5
    print(pt.coordX, pt.coordY)
    print(Point.coordX, Point.coordY)

    print(id(pt.coordX), id(Point.coordX))
