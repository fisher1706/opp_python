class Point:
    def __init__(self, x=0, y=0):
        print('create instance class Point')
        self.x = x
        self.y = y

    def __del__(self):
        print('delete instance: ' + self.__str__())


if __name__ == '__main__':
    pt = Point()

    pt = 0
    print(pt)


