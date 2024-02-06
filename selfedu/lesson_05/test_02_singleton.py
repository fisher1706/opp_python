class DataBase:
    __instance = None

    """
    singleton -> methods: __new__, __del__
    """
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect_db(self):
        print(f"connect to DB: {self.user}, {self.psw}, {self.port}")

    @staticmethod
    def close_db():
        print("close connect with DB")

    @staticmethod
    def read_db():
        print("read data from DB")

    @staticmethod
    def write_db(data):
        print(f"write data to DB {data}")


if __name__ == '__main__':
    db_one = DataBase('root', '1234', 80)
    db_two = DataBase('user', '5678', 40)

    print(id(db_one), id(db_two))

    """
    work with method __call__ for that
    """
    db_one.connect_db()
    db_two.connect_db()
