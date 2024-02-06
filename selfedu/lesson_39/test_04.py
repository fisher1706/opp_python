from dataclasses import dataclass, field, InitVar


@dataclass(repr=False, order=True)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


if __name__ == '__main__':
    v1 = V3D(1, 2, 3)
    v2 = V3D(1, 2, 5)

    print(v1)
    print(v1 < v2)
