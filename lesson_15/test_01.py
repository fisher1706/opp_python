class ThreadData:
    __common_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = ThreadData.__common_attrs


if __name__ == '__main__':
    th1 = ThreadData()
    print(th1.__dict__)

    th2 = ThreadData()
    print(th2.__dict__)

    th2.id = 3
    print(th1.__dict__)
    print(th2.__dict__)

    print(id(th1.__dict__))
    print(id(th2.__dict__))
