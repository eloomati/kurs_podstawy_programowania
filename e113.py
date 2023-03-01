b = 0
a = 4

try:
    print(a)
    y = a / b
except NameError:
    print("Zmienna nie jest zdefiniowana")
except ZeroDivisionError:
    print("Błąd dzielenia przez zero")
except:
    print("Nieokreślony wyjątek")