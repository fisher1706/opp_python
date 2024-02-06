from string import ascii_letters


class Person:
    def __init__(self, fio, old, ps, weight):
        self.__verify_fio(fio)
        self.__verify_old(old)
        self.__verify_ps(ps)
        self.__verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def __verify_fio(cls, fio):
        print("verify_fio")
        if type(fio) != str:
            raise TypeError("must be string")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("wrong format")

        letters = ascii_letters
        for s in f:
            if len(s) < 1:
                raise TypeError("must be symbol")
            if len(s.strip(letters)) != 0:
                raise TypeError("only letter")

    @classmethod
    def __verify_old(cls, old):
        print("verify_old")
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("old mast be int and in [14, 120]")

    @classmethod
    def __verify_weight(cls, weight):
        print("verify_weight")
        if type(weight) != float or weight < 20:
            raise TypeError("weight mast be float and > 20")

    @classmethod
    def __verify_ps(cls, ps):
        print("verify_ps")
        if type(ps) != str:
            raise TypeError("ps must be str")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("wrong ps format")

        for p in s:
            if not p.isdigit():
                raise TypeError("ps must be string")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__old

    @weight.setter
    def weight(self, weight):
        self.__verify_weight(weight)
        self.__weight = weight

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.__verify_ps(ps)
        self.__ps = ps


if __name__ == '__main__':
    person = Person("zapel fisher flagman", 20, '2117 789970', 80.00)

    # print(person.old)
    # person.old = 50
    # print(person.old)
    #
    # print(person.__dict__)
