class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)


if __name__ == '__main__':
    p = Person("oleg", 40)
    p.__dict__["old"] = "old in object p"
    a = p.old
    print(p.old, p.__dict__)

    p.old = 20
    print(p.old, p.__dict__)
