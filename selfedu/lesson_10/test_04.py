class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


if __name__ == '__main__':
    p = Person("oleg", 40)
    print(p.__dict__)

    del p.old
    print(p.__dict__)

    p.old = 20
    print(p.__dict__)
