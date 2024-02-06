class Point:
    WIDTH = 5

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @staticmethod
    def __check_value(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        else:
            return False

    def set_coords(self, x, y):
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('Coords must be number!')

    def get_coords(self):
        return self.__x, self.__y

    def __getattribute__(self, item):
        if item == '_Point__x':
            return 'Private variable'
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'WIDTH':
            raise AttributeError
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print('__getattr__: ' + item)

    def __delattr__(self, item):
        print('__delattr__', item)


if __name__ == '__main__':
    pt = Point(5, 10)
    print(pt.get_coords())
    print(pt._Point__x)

    pt.WIDTH = 5

    pt.z
    pt.z = 1
    del pt.z
