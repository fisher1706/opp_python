def input_example():
    try:
        x, y = map(int, input().split())
        res = x / y
        print(f"res: {res}")
    except (ValueError, ZeroDivisionError) as ex:
        print(f"ex: {ex}")
    else:
        print("that is fine")
    finally:
        print("close")


if __name__ == '__main__':
    input_example()
