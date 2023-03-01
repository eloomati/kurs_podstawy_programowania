class Nums1:

    def calc1(selfs, a, b):
        return a + b

    def calc2(self, a, b):
        return 2 * a + 2 * b

class Nums2(Nums1):

    def calc2(self, a, b):  # Przesłanienie metody calc2() superklasy (klasy bazowej)
        return (2 * a + 2 * b) * 2


ob1 = Nums1()
ob2 = Nums2()
print(ob1.calc1(1, 2))
print(ob1.calc2(1, 2))
print(ob2.calc1(2, 3))
print(ob2.calc2(2, 3))