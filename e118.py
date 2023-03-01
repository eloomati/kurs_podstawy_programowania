a = 5
b = 0

try:
    c = a / b
    print(c)
except:
    raise ZeroDivisionError("Błąd dzielenia przez 0") from None