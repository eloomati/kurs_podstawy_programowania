import pytest

from utpt_calc_mod import TypeOfCalc

class TestTp:
    def test_type_tp1(self):
        t = TypeOfCalc(5, 2)
        pytest.raises(TypeError, t.tp)

    def test_type_tp2(self):
        t = TypeOfCalc(5, 'x')
        pytest.raises(TypeError, t.tp)