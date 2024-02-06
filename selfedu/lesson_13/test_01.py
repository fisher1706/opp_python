class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__counter += 1
        return self.__counter


if __name__ == '__main__':
    c1 = Counter()
    c1()
    c1()
    c1(5)
    res1 = c1()
    print(res1)

    c2 = Counter()
    res2 = c2()
    print(res2)


