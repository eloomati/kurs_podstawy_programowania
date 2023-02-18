#Funkcja sorted

numbers = [3, 4, 5, 9, 11, 97, 0, -123]
#To sortowanie jest nietrwale, poniewaz tworzona jest nowa lista w locie
print(sorted(numbers))
print(sorted(numbers, reverse=True)) #nie sortuje orginalnej listy, jedynie tworzy nowa i ja sortuje
print(numbers)

#krotki sa niezmienialne (niemutowalne)

#Sortuje po pierwszych elementach krotek wewnętrzynych
lt = [(1, 4, 7), (4, 5, 1), (77, 2, 9 ), (2, 3, 5)]
print(sorted(lt))

print(sorted(lt, key=lambda a: a[0]))
print(sorted(lt, key=lambda a: a[2]))
print(sorted(lt, key=lambda a: a[1]))

print(len(lt[1]))
print(lt[0][0])

# Zsumowac elemnty krotek wewnatrznych, wlozyc je na liste i liste sum posortowac
summary = []

for i in lt:
    s = sum(i)
    summary.append(s)

print(sorted(summary))

summary = []
s = 0

for el in lt:
    print(el)
    for e in el: # nested loop (petla, zagniezdzona, wewnetrzna iterujaca po krotce i sumujaca jej elemty
        print(e)
        s += e
    summary.append(s)
    s = 0

print(sorted(summary))