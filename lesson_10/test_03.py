class MyIter:
    def __init__(self, limit):
        self.__num = 0
        self.__limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.__num >= self.__limit:
            raise StopAsyncIteration

        self.__num += 1
        return self.__num


if __name__ == '__main__':
    it = MyIter(10)
    for i in it:
        print(i)
