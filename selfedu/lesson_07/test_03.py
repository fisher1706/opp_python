"""
_ - protested
__ - private
"""
from accessify import private, protected


class Point:
    def __init__(self, x, y):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def check_value(cls, val):
        return type(val) in (int, float)

    def set_coord(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("coords must be digital")

    def get_coord(self):
        return self.__x, self.__y


if __name__ == '__main__':
    pt = Point(1, 2)
    pt.check_value(5)
