"""
Koniunkcja logiczna warunkuje nam wykonanie instrukcji wewnątrz ciała pętli od spełnienia
bądź nie obydwu warunków jednocześnie: w moemencie niespełnienia pierwszego z warunków
(do którego niespełnienia dojdzie szybciej) drugi warunek nie jest już kontynuowany
gdyż wartość logiczna całego wyrażenia jest w tym momencie False
"""
a = 5
b = 10

while a < 20 and b < 40:
    a += 1
    b += 1
    print(a, b)

a = 5
b = 10
print("\n\n")

"""
Alternatywa logiczna 'ot' diametralnie zmienia nam działanie pętli, bo pomimo, że pierwszy
warunek w pewnym momencie przestaje być spełniony to drugi jest spełniany nadal i a zostaje nadal zwiększane
ponieważ alternatywa jest prawdziwa gdy co najmniej jest z podwarunków jest prawdziwy
"""

while a < 20 or b < 40:
    a += 1
    b += 1
    print(a, b)