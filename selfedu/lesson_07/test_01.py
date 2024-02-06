"""
_ - protested
__ - private
"""


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


if __name__ == '__main__':
    pt = Point(1, 2)
    print(pt._x, pt._y)
