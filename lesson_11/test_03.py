def StripChars(chars):
    def stripString(string):
        if not isinstance(string, str):
            raise ValueError('arg must be string')
        return string.strip(chars)
    return stripString


if __name__ == '__main__':
    s1 = StripChars('?:!.:')
    print(s1('Hello World!'))

    s2 = StripChars('?:!.:')
    print(s1('Hello!'))

    print(id(s1), id(s2), sep='\n')