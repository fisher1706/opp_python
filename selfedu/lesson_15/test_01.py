class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise ValueError('secs must be int')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24

        return f'{Clock.__get_formatted(h)}:{Clock.__get_formatted(m)}:{Clock.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def get_seconds(self):
        return self.seconds

    def __add__(self, other):
        print("__add__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('right part must be type Clock or int')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('right part must be type Clock or int')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds += sc
        return self


if __name__ == '__main__':
    c1 = Clock(8000)
    c2 = Clock(1000)

    print(c1.get_time())
    print(c1.get_seconds())

    print((c1 + c2).get_time())

    print((c1 + 100 + c2).get_time())

    c1 += 100
    print(c1.get_time())
