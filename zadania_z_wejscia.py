import random

#ZAD1
#x = input("Jaka jest twoja ulubiona liczba? Podaj: ")
#print(f"Twoja ulubiona liczba to {x}")

#ZAD2
#x = input("Podaj liczbe: ")

#if int(x) % 3 == 0:
#    print("Liczba dzieli sie przez 3")
#else:
#    print("Nie dzieli sie przez 3")

#ZAD3
x = random.randrange(1, 3)
y = int(input("Podaj swoj numer z dziennika: "))

print(x)
if x == y:
    print("Dzis nie bedziesz pytany")
else:
    print("Przygotyh się do odpowiedzi")

#ZAD4
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a + b > c:
    print("Mozna zrobic trojkat")
else:
    print("Taki trojkat nie istnieje")

#ZAD5
x = int(input("Podaj wartosc do obliczenia: "))
calc = 2 * x ** 3 + 5 * x ** 2 + 9 * x + 4
print(calc)