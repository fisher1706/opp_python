class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        print("__getitem__")
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("incorrect index")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("index must be int or index must be > 0")
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("index must be int")
        del self.marks[key]


if __name__ == '__main__':
    s1 = Student("oleg", [3, 5])
    print(s1.marks[0])

    print(s1[0])

    s1[0] = 8
    print(s1.marks)

    s1[10] = 7
    print(s1.marks)

    del s1[1]
    print(s1.marks)
