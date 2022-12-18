class Point:
    """class for present points"""
    x = 1
    y = 1


class Point3D:
    pass


if __name__ == '__main__':
    print(Point.__doc__)
    print(Point.__name__)
    print(dir(Point))

    pt = Point()
    print(pt.__dict__)

    Point.x = 100

    print(pt.x, pt.y)
    print(id(pt), id(Point), sep='\n')

    pt.x = 5
    pt.y = 10

    print(pt.x, Point.x)
    print(pt.__dict__)

    print(getattr(pt, 'x'))
    print(getattr(pt, 'z', False))
    print(hasattr(pt, 'z'))
    print(hasattr(pt, 'y'))

    setattr(pt, 'z', 10)
    print(pt.__dict__)

    delattr(pt, 'z')
    print(pt.__dict__)

    Point.z = 100
    pt.msg = 'hello'

    print(pt.__dict__)

    del pt.x
    print(pt.__dict__)

    print(isinstance(pt, Point))
    print(isinstance(pt, Point3D))


