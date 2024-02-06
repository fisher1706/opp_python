class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


if __name__ == '__main__':
    fr = FRange(0, 2, 0.5)

    # print(fr.__next__())
    # print(fr.__next__())
    # print(fr.__next__())
    # print(fr.__next__())

    """ OR """

    print(next(fr))
    print(next(fr))
    print(next(fr))
    print(next(fr))
