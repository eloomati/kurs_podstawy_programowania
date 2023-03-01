from utpt_float_mod import FloatVal

class TestFloatVal:

    def test_refuling(self):
        f = FloatVal(45, 7.16)
        assert f.refueling() == type(.1)