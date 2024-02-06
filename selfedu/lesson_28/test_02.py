class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    pass


if __name__ == '__main__':
    pt3 = Point3D(10, 20)
    pt3.z = 30
    print(pt3.__dict__)
