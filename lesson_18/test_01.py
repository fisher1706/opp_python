import math


class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = math.sqrt(x * x + y * y)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


class Point3D(Point2D):
    __slots__ = 'z'

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


if __name__ == '__main__':
    pt = Point2D(1, 2)
    print(pt.length)

    pt.length = 10
    print(pt.length)

    pt3 = Point3D(10, 20, 50)
    pt3.z = 30
    print(pt3.z)
    # print(pt3.__dict__)
    print(pt3.__slots__)

    del pt3.x
    pt3.x = 10
    # print(pt3.__dict__)
