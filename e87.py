i = 97

def fun(x):
    global i
    i = 3
    j = 5
    return x ** i

print(i) # Zmienna i jeszcze nie została zmodyfikowana przez funkcje
print(fun(2)) # Zmienna i została zmodyfikowana przez funkcję i słowo global
print(i) # Zmienna i została zmodyfikowana przez funckję i słowo global, więc mogę wywołać ją z wnętrza funkcji
# print(j) # NameError: zmienna j jest lokalna i nie jest widoczna poza funkcją