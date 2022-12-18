class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def getPerimeter(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def getPerimeter(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getPerimeter(self):
        return self.a + self.b + self.c


if __name__ == '__main__':
    r1 = Rectangle(1, 2)
    r2 = Rectangle(3, 4)

    s1 = Square(10)
    s2 = Square(20)

    t1 = Triangle(1, 2, 3)
    t2 = Triangle(4, 5, 6)

    geom = [r1, r2, s1, s2, t1, t2]

    for g in geom:
        print(g.getPerimeter())
