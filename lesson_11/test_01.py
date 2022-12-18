class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        self.__counter += 1
        print(self.__counter)
        return self.__counter


if __name__ == '__main__':
    c1 = Counter()
    c1()