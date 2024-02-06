class Point:
    """class for present points"""
    color = "red"
    circle = 1


class Point3D:
    pass


if __name__ == '__main__':
    print(Point.__doc__)
    print(Point.__name__)
    print(Point.__dict__)

    a = Point()
    b = Point()

    print(type(a))
    print(isinstance(a, Point))

    print(a.__dict__)
    print(a.color)

    a.color = "green"

    print(a.color)
    print(b.color)
    print(Point.color)
    print(a.__dict__)

    Point.type_pt = 'disc'
    print(Point.__dict__)

    setattr(Point, 'prop', 1)
    print(Point.__dict__)

    print(hasattr(Point, 'prop'))

    del Point.prop
    print(Point.__dict__)

    print(getattr(Point, 'a', False))

    delattr(Point, 'type_pt')
    print(Point.__dict__)
