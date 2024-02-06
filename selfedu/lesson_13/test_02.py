class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("arg must be str")
        return args[0].strip(self.__chars)


if __name__ == '__main__':
    s = StripChars("?:!.; ")
    res = s(" Hello World! ")
    print(res)
