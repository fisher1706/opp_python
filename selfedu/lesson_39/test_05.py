from dataclasses import dataclass, field


@dataclass(frozen=True)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    length: float = field(init=False, compare=False, default=0)


if __name__ == '__main__':
    v1 = V3D(1, 2, 3)

    print(v1)
