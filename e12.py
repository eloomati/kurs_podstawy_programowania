#METODA FSTRINGU
# : (dwukropek) operator morsa/operator przypisania
from math import sqrt, e

a = 1
string = f"Liczba a jest równa {a}."
a = 5
print(string)

b = 3
tab = "\t\t\t"
res = 3 // 2
string1 = f"{(c:=sqrt(b))}{tab}{c}\n{res}\n"
print(string1, c)

print(f"{e:@>25.5f}|{e:*^25.5e}")

print("--------------------------")
x = 1
y = 2
print("Liczba mniejsza zmieści się:", y // x, "razy")
print("--------------------------")

x = 1
y = 2
res = (x+y)/2
string = f"Średnia arytmetyczna to: {res}."
print(string)
print("--------------------------")

m = 90
g_earth = 8.91
q = m * g_earth
g_merc = (37.8 * q)/100
g_jupiter = (252.8 * q)/100

string = f"Jeśli na Ziemi ważysz: {q} to na merkurym: {g_merc},a na jowiszu: {g_jupiter}"
print(string)