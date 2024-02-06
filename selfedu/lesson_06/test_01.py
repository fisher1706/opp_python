class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm_two(x, y):
        return x*x + y*y

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm_two(x, y))

    def get_coord(self):
        return self.x, self.y


if __name__ == '__main__':
    v = Vector(1, 2)

    res_one = v.get_coord()
    print(res_one)

    res_two = Vector.get_coord(v)
    print(res_two)

    print(Vector.validate(5))
    print(v.validate(3))

    print(Vector.norm_two(5, 6))
    print(v.norm_two(3, 4))


