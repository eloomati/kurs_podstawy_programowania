#PETLA FOR e23-e26
#for i in range(10_000):
 #   print(i)

n = 5
for i in range(n): #wypisze liczby <0;n)
    print(i)
print("-----------------------------")

for i in range(3,n): #wypisze liczby <3; n)
    print(i)
print("-----------------------------")

for i in range(5, 20, 2): #wypsize liczby <5; 20) z krokiem równym 2 (co 2) -> inkrementacja (zwiększanie w górę)
    print(i)
print("-----------------------------")

for i in range(20, 5, -2): #wypisze liczby <20;5) z krokiem równym -2 (co -2) -> dekrementacja (schodzenie w dół)
    print(i)
print("-----------------------------")

for _ in range(n): # _ zmienna tymaczowa, temperary. Używamy gdy chcemy zazaczyć, że jest to zmienna iteracyjna tymczasowa zamiast i
    print(_)