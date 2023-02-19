from math import sqrt, pi

#ZAD1
temp = - 24
if temp >= 0:
    print("Brak mrozu")
else:
    print("Jest mróz")
    #wynik jest zgodny z oczekiwaniami. Jest mroz
#ZAD2
#if dotyczy 3 instrukcji if
#ZAD3
#a
a = "fraza 1"
b = "fraza2"

if a == b:
    True
else:
    False
#b
a = 0
b = 0

if a == b:
    True
else:
    False

#c
name = "Mati"

if name != 0:
    print(name.upper())
    True
else:
    False

#d
x = 1
y = 0

if x != 0 or y !=0:
    True
else:
    False

#ZAD4
salary = 2000

if 2000 <= salary <= 3000 or 4000 <= salary <= 7000:
    print("Miescie się")
else:
    print("Nie zarabiasz odpowiednio")

#ZAD5
engineer = 20

if 0 <= engineer < 10:
    print("Musimy zaczekac")
elif 10 <= engineer < 20:
    print("Niewystarczajaca ilosc")
elif engineer >= 20:
    print("Optymalnie")
else:
    print("Niewłaściwe dane!")

#ZAD6
object_type = "Rakieta"

if object_type == "Rakieta":
    print("Obiekt nr.1")
elif object_type == "sonda_kosmiczna":
    print("Obiekt nr. 2")
elif object_type == "stacja_kosmiczna":
    print("Obiekt nr.3")

#ZAD7
age = 25

if age < 7:
    print("Nie chodzisz jeszcze do szkoły")
elif 7 <= age < 15:
    print("Chodzisz do szkoły podstawowej")
elif 15 <= age < 20:
    print("Chodzisz do szkoły średniej")
elif 20 <= age < 25:
    print("Jesteś studentem")
elif age >= 25:
    print("Twoja edukacja się zakończyła")

#ZAD8
x = 13

if x >= 0:
    print("Wieksza od 0")

if x> 5:
    print("Wieksza od 5")

if x % 2 == 0:
    print("Podzielna przez dwa")
else:
    print("Nie podzielna")

if x % 2 != 0:
    print("Nieparzysta")
else:
    print("Parzysta")

#ZAD9
x = -1

if x > 0:
    print("Dodatnia")
else:
    print("Ujemna")

#ZAD10
x = -5-2

if x > 0:
    print(x)
else:
    x = x * -1
    print(x)

#ZAD11
temp = 0

if temp > 70:
    print("PROCESOR SIE PRZEGRZEWA")
else:
    print("Temperatura w normie")

#ZAD12
engineer = 5
temp = 270
pres = 75

if engineer >= 5 and temp < 280 and pres == 75:
    print("Reaktor gotowy")
else:
    print("Trzeba czekac")

#ZAD13
math_mark = 4
cs_mark = 5

if 4 <= math_mark <= 5 and 4 <= cs_mark <= 5:
    print("Dostałeś się")
else:
    print("Popracuj")

#ZAD14
wheel = 4
fuel = 10

if wheel == 4 and fuel > 0:
    print("Mozna jechac")
else:
    print("Czegos brakuje")

#ZAD15
#a * x ** 2 + b * x + c = 0
#a>0
# delta = b ** 2 - 4 * a * c
# delta > 0
# x1 = (- b - sqrt delta) / 2 * a
# x2 = (- b + sqrt delta) / 2 * a
# delta = 0
# x = -b / 2 * a
# delta < 0 nie ma pierwiastkow
a = 1
b = 5
c = 3

delta = b ** 2 - 4 * a * c
print(delta)
if delta > 0:
    x1 = (-b - sqrt(delta)) / 2 * a
    x2 = (-b + sqrt(delta)) / 2 * a
    print(x1, x2)
elif delta == 0:
    x0 = -b / 2 * a
    print(x0)
else:
    print("Nie ma miejsc zerowych")

#ZAD16
a = 2
b = 6
c = 5

if a > c and b > a:
    x = a * b
    print(x)
elif b < c or b < a:
    x = b / c
    print(x)
elif c > a and b != 5 or b > c and a != 0:
    x = a + b + c
    print(x)

#ZAD17
a = 0
b = 1

if a > b:
    print(a-b)
else:
    print(a*b)

x = 16

if 5 <= x <= 15:
    print(pi)
elif x > 15:
    print((x + 2)*(x - 3))
else:
    print("Nie ma wyniku")

#ZAD18
#a ** 2 + b ** 2 = c ** 2

a = 3
b = 4
c = 5

if a ** 2 + b ** 2 == c ** 2:
    print("Trojkat jest prostokatny")
else:
    print("Trojkat nie jest prostokatny")

#ZAD19
a = 1
b = 1
c = 2
h = 0
sin = 0

if a > 0 and h > 0:
    print((a * h ) / 2)
elif a > 0 and b > 0 and sin > 0:
    print((a * b * sin) / 2)
elif a > 0 and b > 0 and c > 0:
    p = (a + b + c) / 2
    print(p)
    x = p * ((p - a) * (p - b) * (p - c))
    print(x)
else:
    print("Twoje dane sa niepoprawne")

#ZAD20
tf = 0
tc = 0
tk = 0

if tf > 0:
    print(0.56 * (tf - 32), "stopni Celcjusza")
elif tc > 0:
    print(273.15 + tc, "stopni Kelwina")
else:
    print(tk, "stopni Kelwina")

#ZAD21
a = 1
b = 2
c = 3

if c > b > a:
     print("liczby są wprowadzane w porządku niemalejącym")
else:
    print("Zmien kolejnosc")