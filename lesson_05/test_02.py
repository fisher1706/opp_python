class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        Point.__count += 1
        self.coordX = x
        self.coordY = y

    @staticmethod
    def getCount():
        return Point.__count


if __name__ == '__main__':
    pt1 = Point()
    pt2 = Point()
    print(pt2.getCount(), Point.getCount())
