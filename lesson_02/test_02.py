class Point:
    x = 1
    y = 1

    def setCoords(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    pt = Point()
    print(pt.__dict__)

    pt.setCoords(5, 10)
    print(pt.__dict__)

    Point.setCoords(pt, 3, 4)
    print(pt.__dict__)
