class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property()
    old = old.setter(set_old)
    old = old.getter(get_old)


if __name__ == '__main__':
    p = Person("oleg", 40)
    print(p.old, p.__dict__)
