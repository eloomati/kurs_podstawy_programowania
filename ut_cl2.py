from unittest import TestCase

from ut_mod_cubes import Cubes

class TestCubes(TestCase):

    def setUp(self):
        self.c = Cubes()
    # POzwala ustalić zmienną przed testami, usprawnia to kod i jego przejrzystość
    def test_show_cubes(self):
        self.c.cubes(1, 2, 3, 4, 434, 34, 22, 23, 2, 1)
        self.c.show_cubes()
        self.assertIn(22 **3, c.lst_cubes)