from unittest import TestCase

from ut_mod_data import get_data_3

class DataTest(TestCase):
    def test_first_last_occ1(self):
        data = get_data_3("Gary", "Feedbacker")
        self.assertEqual(data, 'Gary Feedbacker')
    def test_first_last_occ2(self):
        data = get_data_3("Gary",
                          "Feedbacker", "programista")
        self.assertEqual(data,
                         'Gary Feedbacker, Programista')