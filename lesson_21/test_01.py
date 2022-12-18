class ExceptionPrint(Exception):
    """base class exception printer"""


class ExceptionPrintSendData(ExceptionPrint):
    """class for Exception"""

    def __init__(self, *args):
        super().__init__(*args)
        self.msg = args[0] if args else None

    def __str__(self):
        return f"error: {self.msg}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"print: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            # raise Exception('printer is not answer')
            raise ExceptionPrintSendData('printer is not answer')

    def send_to_print(self, data):
        return False


if __name__ == '__main__':
    p = PrintData()
    # p.print('123')

    try:
        p.print('123')
    except ExceptionPrintSendData as e:
        print(e)
    except ExceptionPrint:
        print('error')
