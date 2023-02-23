def fun_Lin(x):
    return 5 * x + 1
print(fun_Lin(3))

xs = list(range(1_000))
print(list(map(fun_Lin, xs))) # Funkcja map() mapuje jakąś funkcję (tutaj fun_lin()) na każdym elemencie listy xs

# Alternatywnie mogę powyższą linijkę zrobić tak:
fun_Lin_lst = []
for x in xs:
    fun_Lin_lst.append(fun_Lin(x))

print(fun_Lin_lst)