class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id} - was selled at 00-00")

    def print_info(self):
        print(f"id: {self.id}")


class NoteBook(Goods, MixinLog):
    def print_info(self):
        MixinLog.print_info(self)


if __name__ == '__main__':
    n = NoteBook("Acer", 1.5, 30000)
    n.save_sell_log()
    n.print_info()

    MixinLog.print_info(n)

    print(NoteBook.__mro__)
