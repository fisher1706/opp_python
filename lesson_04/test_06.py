class NoDataDescr:
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return 'NoDataDescr __get__'


class CoordValue:
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Point:
    noData = NoDataDescr()

    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


if __name__ == '__main__':
    pt = Point(1, 2)
    pt.coordX = 5
    print(pt.coordX, pt.coordY)

    pt.noData = 'hello'

