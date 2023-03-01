class FloatVal:
    def __init__(self, fuel, price):
        self.fuel = fuel
        self.price = price

    def refueling(self):
        return type(self.fuel * self.price)