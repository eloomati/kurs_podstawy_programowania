from math import pi, inf

#ZAD1
for i in range(0,20):
    print(f"Liczba{i}")
    if i >= 15:
        break
#Zadaniem programu jest wypisywać liczbę i w zakresie od 0 do 20, ale przy
#i wikeszym lub ronwym 15 wyjscie z petli przez break i zakonczenie pracy
#wszystko to w efekcie wypisze liczby od 0 do 15

#ZAD5
earth_weight = 0

for i in range(0, 21):
    jupiter_weight = 2.54 * earth_weight
    print(f"Waga po {i} roku wynosi {jupiter_weight}")
    earth_weight += 1

#ZAD7
i = 0
for x in range(0, 101):
    y = 5 * int(x) - 15
    if y == 0:
        i += 1
        print(x, i)

#ZAD8
for i in range(1, 41):
    print(i)

j = 1
while j < 41:
    print(j)
    j += 1

#ZAD9
for i in range(40, 0, -1):
    print(i)

j = 40
while j >= 1:
    print(j)
    j -= 1

#ZAD10
for i in range (1,101):
    print("Python"*i)

j = 0
while j <= 100:
    print("PYTHON")
    j += 1

#ZAD11
sum = 0
for i in range(1, 51):
    sum += i
print(sum)

j = 0
while j <= 50:
    print(j)
    sum += j
    j += 1
print(sum)

#ZAD12
for i in range(0,21):
    if i % 2 != 0:
        print("Informatyka")
    else:
        print("")

j = 0

while j <=20:
    if j % 2 != 0:
        print("Informatyka")
    else:
        print("")
    j += 1

#ZAD13

i = 1
h = 0

while i <= 1_000_000_000:
    i = i * 2
    h += 1

print(h)

#ZAD19
for i in range(5, 21):
    ob = 2 * pi * i
    print(f"Kolo o promieniu {i} ma obwód o długości: {round(ob, 3)}")

#ZAD20
a = 4
for i in range (0, 5):
    p = a ** 2
    a *= 2
    print(p)

#ZAD21
counter = 0
sum = 0
for i in range(0, 41):
    sum += i
    print(sum)
    if sum % 2 == 0:
        counter += 1
print(counter)

#ZAD22
sum = 0
for i in range (0, 21):
    sum += i
    average = sum / 2
    print(sum, "\n", average)

#ZAD23
n = int(input("Podaj liczbe"))

for i in range(1, 5):
    x = n * i
    print(x)

#ZAD24
login = input("Podaj login: ")
counter = 0

while counter <= 1:
    if login != '':
        print(login)
        pwd = input("Podaj haslo: ")
        if pwd != '':
            print(f"Witaj {login}!")
            break
        else:
            counter += 1
            continue
    else:
        counter = 1
        counter += 1
        login = input("Podaj login: ")
        continue
else:
    print("Nieudana proba logowania")

#ZAD26
num = input("Enter zeby zaczac!")
i = 0
while num != 0:
    num = int(input("Podaj liczbe: "))
    if num == 3:
      i += 1

print(i)

#ZAD27
sum = 0
for i in range (0, 901):
    print(i)
    if i % 2 == 0 and i % 6 == 0:
        sum += 1

print(sum)

#ZAD28
for i in range(4, 14):
    for j in range(1, 10_000):
        calc = i * j
        if calc >= 10_000:
            break
        else:
            print(calc)

#ZAD29

for i in range(20, -31, -5):
    print(i)

#ZAD30
for i in range(2, 1001):
    if i % 2 == 0:
        print(i)

#ZAD31
for i in range(1, 101):
    if i % 3 == 0:
        print(i)

#ZAD32
for i in range(1, 21):
    if i % 2 == 0:
        i *= -1
        print(i)
    else:
        print(i)

#ZAD33 DUZOOOOOO PYTAN
j = 40
while j >= 0:
    print(j)
    j -= 1

for i in range(0, 41):
    print(i)

if i == j:
    print("Są równe")

#ZAD34
#(n-1)*n
