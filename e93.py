lst1 = list(range(100))
"""
Funkcja anonimowa lambda ma następującą składnie: lambda parametr(y): treść funkcji
W poniższym przykładzie tworzymy listę lst2 na którą odkładane będą elementy listy lst1 uprzednio
zmodyfikowane funkcją lambda (tutaj zwracającą kwadrat parametru)
"""

lst2 = list(map(lambda x: x ** 2, lst1))
print(lst2)

nums = [1, 2, 3, 4, 8, 7, 9, 234, 77, 88, 236, 567]

def fun(n):
    if n % 2 == 0:
        return True
    return False

#Test
print(fun(8), fun(3))

even = filter(fun, nums)
# Sprawdzenie, czym jest even (obiekt w pamięci, co prawda nie lista i nie krotka ale można iterować
print(even)

for e in even:
    print(e)

def fun_1(n):
    if n % 2 != 0:
        return True
    return False

odd = filter(fun_1, nums)

for o in odd:
    print(o)

list_nums=list(range(101))
print(list(filter((lambda x:(x%2!=0)),list_nums)))