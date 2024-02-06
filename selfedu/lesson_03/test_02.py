class Point:
    x = 1
    y = 1

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


if __name__ == '__main__':
    pt = Point()
    print(pt.__dict__)

    pt.set_coords(5, 10)
    print(pt.__dict__)

    Point.set_coords(pt, 3, 4)
    print(pt.__dict__)

    print(pt.get_coords())
