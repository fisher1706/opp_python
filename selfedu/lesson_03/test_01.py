class Point:
    x = 1
    y = 1

    def set_coords(self):
        print(self.__dict__, str(self))


if __name__ == '__main__':
    pt = Point()
    pt.set_coords()

    pt.x = 5
    pt.y = 10
    pt.set_coords()

    Point.set_coords(pt)
