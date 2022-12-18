class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def setCoords(self, x, y):
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    @classmethod
    def validate(cls, arg):
        if cls.MIN_COORD <= arg <= cls.MAX_COORD:
            return True
        return False

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


if __name__ == '__main__':
    v = Vector()
    v.setCoords(10, 20)

    print(v.norm2(10, 20))

