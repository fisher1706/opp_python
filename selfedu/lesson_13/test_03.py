import math


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        print("__call__")
        return (self.__fn(x + dx) - self.__fn(x)) / dx


def df_sin(x):
    return math.sin(x)


if __name__ == '__main__':
    df_sin = Derivate(df_sin)
    print(df_sin(math.pi/4))
