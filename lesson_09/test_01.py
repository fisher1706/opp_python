class Clock:
    __DAY = 86400

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError('secs must be int')

        self.__secs = secs % self.__DAY

    def getFormatTime(self):
        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 3600) % 24

        return f'{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}'

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else '0' + str(x)

    def getSeconds(self):
        return self.__secs

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('right part must be type Clock')

        return Clock(self.__secs + other.getSeconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('right part must be type Clock')
        self.__secs += other.getSeconds()

        return self

    def __eq__(self, other):
        return self.__secs == other.getSeconds()

    def __nq__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError('key must be string')

        if item == 'hour':
            return (self.__secs // 3600) % 24
        elif item == 'min':
            return (self.__secs // 60) % 60
        elif item == 'sec':
            return self.__secs % 60

        return 'bad key'

    def __setitem__(self, key, value):
        if not isinstance(value, str):
            raise ValueError('key must be string')

        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 3600) % 24

        if key == 'hour':
            self.__secs = s + 60 * m + value * 3600
        elif key == 'min':
            self.__secs = s + 60 * value + h * 3600
        elif key == 'sec':
            self.__secs = value + 60 * m + h * 3600


if __name__ == '__main__':
    c1 = Clock(8000)
    print(c1.getFormatTime())

    c2 = Clock(8000)
    print(c2.getFormatTime())

    c3 = c1 + c2
    print(c3.getFormatTime())

    c1 += c2
    print(c1.getFormatTime())

    if c1 == c2:
        print('time equal')

    print(c1['hour'])
