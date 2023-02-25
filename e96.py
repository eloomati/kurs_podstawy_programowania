class Rectangle:
    """Modelowanie prostokąta"""


    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color
        self.num_of_sides = 4

    def rectangle_color(self):
        print(f"Mam kolor: {self.color}")

    def rectable_cicrcuit(self):
        cicrcuit = 2 * self.a + 2 * self.b
        print(f"Mój obwód wynosi: {cicrcuit}")

    def rectangle_area(self):
        area = self.a * self.b
        print(f"Moja pole jest równe: {area}")

    def print_num_of_sider(self):
        print(f"Prostokąt ma {self.num_of_sides} boki")


r1 = Rectangle(2, 5, "zielony")

print(f"Prostoką o bokach {r1.a}, {r1.b}: ")
r1.rectangle_color()
r1.rectable_cicrcuit()
r1.rectangle_area()
r1.print_num_of_sider()

r2 = Rectangle(10, 14, "czarny")
print(f"Prostokąt o bokach {r2.a}, {r2.b}")
r2.rectangle_color()
r2.rectable_cicrcuit()
r2.rectangle_area()
r2.print_num_of_sider()