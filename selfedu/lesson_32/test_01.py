class ExceptionPrint(Exception):
    print("hello from ExceptionPrint")


class ExceptionPrintSendData(ExceptionPrint):
    print("hello from ExceptionPrintSendData")

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Error: {self.message}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"print: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("printer is nor answer")

    @staticmethod
    def send_to_print(data):
        print(f"data: {data}")
        return False


if __name__ == '__main__':
    pd = PrintData()

    try:
        pd.print("zapel")
    except ExceptionPrintSendData as ex:
        print(f"printer not found - reason: {ex}")
    except ExceptionPrint:
        print("main error printing")

    pd.print("oleg")
