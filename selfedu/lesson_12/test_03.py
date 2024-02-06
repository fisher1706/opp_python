class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("coord must be int")

    def __set_name__(self, owner, name):
        print(f"__set_name__: {name}")
        self.name = "_" + name

    def __get__(self, instance, owner):
        print(f"__get__: {self.name}")
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f"__set__: {self.name} = {value}")
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


if __name__ == '__main__':
    p = Point3D(1, 2, 3)

    p.x = 30

    print(p.xr, p.__dict__)

    print(p.x)

    p.xr = 5
    print(p.__dict__)
