class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @staticmethod
    def __check_value(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        else:
            return False

    def set_coords(self, x, y):
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('Coords must be number!')

    def get_coords(self):
        return self.__x, self.__y


if __name__ == '__main__':
    pt = Point(5, 10)
    print(pt.__dict__)

    pt.set_coords(10, 20)
    print(pt.__dict__)
    print(pt.get_coords())

    print(pt._Point__x)

    print(Point._Point__check_value(4))
