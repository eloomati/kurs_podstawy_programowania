a = 12
b = 6
mult = 7 * a

if mult < 1000:
    print(mult)
    print(b)
else:
    print(a*b)

#analogiczny algorytm to powyższego, tylko używa operatora := (czyli operator morse'a, walrus operator)
#operator ten służy do przypisawanie wyników działań do zmiennej w "locie", to znaczy w obrębie samej
#intrukcji np. warunkowej
#na dole bardziej polecany
if mult := 7 * a < 1000:
    print(mult)
    print(b)
else:
    print(a*b)