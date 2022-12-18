class Point:
    x = 1
    y = 1

    def setCoords(self):
        print(self.__dict__)


if __name__ == '__main__':
    pt = Point()
    pt.setCoords()

    pt.x = 5
    pt.y = 10
    pt.setCoords()
    