from dataclasses import dataclass


@dataclass(init=False)
class V3D:
    x: int
    y: int
    z: int


if __name__ == '__main__':
    v1 = V3D()
    print(v1.__dict__)
