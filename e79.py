def s(a, b):
    return a + b

print(s(2, 3))

s(2, 3)
def s1(a, b):
    """Moja funkcja zwracająca sumę 2 liczb"""
    c = a + b
    print(c)  # Printując wypisuję tylko obiekt, ale nie mogę go później (poza funkcją) użyć w obliczeniach
    return c  # Returnując rzeczywiście zwracam obiekt w sensie matematycznym


result = s1(2, 3) + 7
print(result)

print(s1.__doc__)
print(len.__doc__)
print(print.__doc__)

def id(first_name, second_name):
    print(f"Witaj {first_name} {second_name}")


id("Mateusz", "Hetko")