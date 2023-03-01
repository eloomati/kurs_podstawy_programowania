class Divide:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def divide_nums(self):
        if self.b == 0:
            raise ZeroDivisionError
        return self.a / self.b