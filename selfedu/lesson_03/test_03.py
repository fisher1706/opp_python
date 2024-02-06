class Point:
    def __init__(self, x=0, y=0):
        print('create instance class Point')
        self.x = x
        self.y = y

    def __del__(self):
        print('delete instance: ' + self.__str__())


if __name__ == '__main__':
    pt_1 = Point(5, 10)
    print(pt_1.__dict__)

    pt_2 = Point()
    print(pt_2.__dict__)

