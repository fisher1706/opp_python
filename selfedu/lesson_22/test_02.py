class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


if __name__ == '__main__':
    v = Vector([1, 2, 3])

    print(v)
