class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update(
            {
                "MAX_COORD": 100,
                "MIN_COORD": 0
            }
        )
        return type.__new__(cls, name, base, attrs)


class Point(metaclass=Meta):
    @staticmethod
    def get_coords():
        return 0, 0


if __name__ == '__main__':
    pt = Point()

    print(pt.MAX_COORD)
    print(pt.get_coords())
