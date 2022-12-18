class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


if __name__ == '__main__':
    pt = Point(5, 10)
    print(pt.__dict__)
    print(pt.x, pt.y)

    pt.x = 100
    print(pt.__dict__)
