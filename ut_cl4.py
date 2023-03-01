import unittest

from ut_ar_mod import Divide

class TestDivide(unittest.TestCase):

    def test_divide_nums(self):
        d1 = Divide(4, 0)
        self.assertRaises(ZeroDivisionError, d1.divide_nums)

    def test_divide_nums_message(self):
        d2 = Divide(76, 0)
        # Teraz sprawdzane są dwa aspekty działania metody assertRaisesRegex():
        # po pierwsz czy zwróci ZeroDivisionError, a po drugie
        # czy jako komunikat zwróci pusty string
        self.assertRaisesRegex(ZeroDivisionError, "", d2.divide_nums)