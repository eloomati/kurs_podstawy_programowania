from functools import reduce


# Funkcja reduce() redukuje listę do końcowej liczby w ten sposób, że pobiera pierwszy i drugi element listy
# następnie zwraca wynik, po czym pobiera wynik i trzeci, zwracając kolejny wynik, następnie
# czwarty itd. aż do uzyskania pojedynczej końcowej liczby (ostatecznego wyniku). Funkcja ta musi mieć 2 parametry.
# W poniższym przykładzie zwraca tak naprawdę silnię z 5
lst = [1, 2, 3, 4, 5]
el = reduce(lambda x, y: x * y, lst)
print(el)

nums = range(1, 101)

def fun(a, b):
    return a + b

# Liczy sumę ciągu arytmetycznego od 1 do 100
print(reduce(fun, nums))

print(reduce(lambda a, b: a + b, nums))