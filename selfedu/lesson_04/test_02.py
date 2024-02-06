class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coords(self, x, y):
        if isinstance(x, int) or isinstance(x, float) and isinstance(y, int) or isinstance(y, float):
            self.__x = x
            self.__y = y
        else:
            print('Coords must be number!')

    def get_coords(self):
        return self.__x, self.__y


if __name__ == '__main__':
    pt = Point(5, 10)
    print(pt.__dict__)
    # print(pt.__x)

    pt.set_coords(10, 20)
    print(pt.__dict__)
    print(pt.get_coords())

    pt.set_coords('10', 20)
