def get_value():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as ex:
        print(f"ex: {ex}")
        return 0, 0
    finally:
        print("do [finally]")


if __name__ == '__main__':
    a, b = get_value()
    print(a, b)
    