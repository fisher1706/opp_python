class DefenderVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__tmp = self.__v[:]
        return self.__tmp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__tmp
        # return False
       

if __name__ == '__main__':
    v1 = [1, 2, 3]
    v2 = [1, 2, 3]

    with DefenderVector(v1) as dv:
        for i in range(len(dv)):
            dv[i] += v2[i]

    print(v1)


