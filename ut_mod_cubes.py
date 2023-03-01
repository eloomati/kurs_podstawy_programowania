class Cubes:

    def cubes(self, *numbers):
        self.lst_cubes = []
        print("Podstawy: ")
        for n in numbers:
            print(n)
            self.lst_cubes.append(n ** 3)

    def show_cubes(self):
        print("Sześciany podanych podstaw: ")
        for cube in self.lst_cubes:
            print(cube)