from unittest import TestCase

from ut_mod_cubes import Cubes

class DataTest(TestCase):

    def test_show_cubes(self):
        c = Cubes()
        c.cubes(1, 2, 3, 4, 434, 34, 22, 23, 2, 1)
        c.show_cubes()
        self.assertIn(22 **3, c.lst_cubes) # Metoda ta sprawdza czy jakiś element jest na liście c.lst_cubes