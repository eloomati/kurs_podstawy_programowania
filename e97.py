class Square:
    """ Modelowanie kwadratu"""
    def __init__(self, a):
        self.a = a

        self.num_of_sides = 4

    def square_circum(self):
        circum = self.a * 4
        print(f"Kwadrat ma obwód: {circum}")

    def square_area(self):
        area = self.a ** 2
        print(f"Kwadrat ma pole: {area}")

    def square_sides(self):
        print(f"Kwadrat ma {self.num_of_sides}")

s1 = Square(5)
s1.square_area()
s1.square_sides()
s1.square_circum()