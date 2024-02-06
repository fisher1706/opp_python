class Meta(type):
    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        cls.MAX_COORD = 100
        cls.MIN_COORD = 0


class Point(metaclass=Meta):
    @staticmethod
    def get_coords():
        return 0, 0


if __name__ == '__main__':
    pt = Point()

    print(pt.MAX_COORD)
    print(pt.get_coords())
