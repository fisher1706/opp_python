def create_class_point(name, base, attrs):
    attrs.update(
        {
            "MAX_COORD": 100,
            "MIN_COORD": 0
        }
    )
    return type(name, base, attrs)


class Point(metaclass=create_class_point):
    @staticmethod
    def get_coords():
        return 0, 0


if __name__ == '__main__':
    pt = Point()

    print(pt.MAX_COORD)
    print(pt.get_coords())
