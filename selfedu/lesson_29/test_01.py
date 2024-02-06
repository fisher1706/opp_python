def open_file(name):
    try:
        f = open(name)
        print(f"f: {f}")
    except FileNotFoundError as err:
        print(f"{err}")
    finally:
        print("close")


if __name__ == '__main__':
    open_file("my_file.txt")
    print("*" * 200)

    open_file("file.txt")
