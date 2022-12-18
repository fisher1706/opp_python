class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def getPerRect(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def getPerSq(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getPerTr(self):
        return self.a + self.b + self.c


if __name__ == '__main__':
    r1 = Rectangle(1, 2)
    r2 = Rectangle(3, 4)
    print(r1.getPerRect(), r2.getPerRect())

    s1 = Square(10)
    s2 = Square(20)
    print(s1.getPerSq(), s2.getPerSq())

    t1 = Triangle(1, 2, 3)
    t2 = Triangle(4, 5, 6)
    print(t1.getPerTr(), t2.getPerTr())
