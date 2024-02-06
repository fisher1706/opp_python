class Geom:
    pass


class Line(Geom):
    pass


if __name__ == '__main__':
    geom = Geom()
    line = Line()

    print(line.__class__)
    print(issubclass(Line, Geom))

    print(issubclass(int, object))
