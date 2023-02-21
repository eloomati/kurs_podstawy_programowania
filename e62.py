#listy zagniezdzone

from math import pi, e

mix = [[1, 3, pi], [e, "monday", not True, 'e'], [3.3 +4.5j]]
print(mix[1]) #Wypisuje liste pod pierwsyzm indeksem
print(mix[:1]) #wypisuje pierwszy element
print(mix[1][2])
print(mix[0][1] ** 2)


for el in mix[1]:
    print(el, end='')