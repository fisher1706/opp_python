class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y
        

if __name__ == '__main__':
    pt1 = Point()
    pt2 = Point()
    print(pt1.count, pt2.count)

    Point.count = 10
    print(pt1.count, pt2.count)