def fun_q(x):
    y = x * x
    return y

print(fun_q(765))
print(fun_q(234) + 23232123123123213)

def sum2(a, b):
    sm = a + b
    print(f"Suma: {sm}")

s = sum2(23233, 232432423)
print(s) # Wypisze None, ponieważ s jest "puste", bo funkcja nic nie zwraca returnem

def sum3(a, b, c):
    sm = a + b + c
    print(f"Suma: {sm}")
    return sm

s = sum3(23233, 232432423, 32342342341312311)
print(s + 1) # wypisze samą sumę ponieważ ładnie zwrócimy returnem tą sumę i można ją dodatkowo użyć w jakichś obliczeniach

#print(sm) # Będzie błąd, ponieważ nie mogę wywołać zmiennej z wnętrza funkcji, bo jest to zmienna LOKALNA