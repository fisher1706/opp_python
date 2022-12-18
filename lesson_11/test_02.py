class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError('arg must be string')

        return args[0].strip(self.__chars)


if __name__ == '__main__':
    s1 = StripChars('?:!.:')
    print(s1('Hello World!'))
    