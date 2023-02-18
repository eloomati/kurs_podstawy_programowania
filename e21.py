num = 12
expression = num % 2
print(expression)
"""
Program bada, czy liczba jest parzysta (poprzez operator %). Jeżeli tak, to wiadomo, że resztą z dzielenia
tej liczby przez 2 będzie zawsze 0, a wiemy, że 0 to - z pktu widzenia programistycznego - zawsze fałsz.
Natomkats w momencie gdy otrzymamy 1, to będzie znaczyło po pierwsze, że mamy do czynienia z liczbą nieparzystą
a po drugie, że jest to wartość True. Skoro True to operator ternarny "pójdzie" na lewo wyświetlając
to co jest tam zawarte, w przeciwnym przypadku "pójdzie" na prawo (czyli wtedy gdy wartość w expression będzie
zerem) i wyświetli to co jest na prawo, czyli napis Parzysta
"""
if expression == 1:
    print("Nieparzysta")
else:
    print("Parzysta")

a = "Nieparzysta" if expression else "Parzysta"
print(a)