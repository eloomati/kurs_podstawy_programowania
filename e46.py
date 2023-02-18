waiting = ['eliza', 'jacek', 'magda', 'kasia', 'patryk', 'krzysztof', 'szymon']
let_in = []
print(waiting)
"""
Pętla while działa (iteruje, powtarza) w kółko operacje dopóki dopóty lista waiting jest zapełniona
(czyli zawiera co najmniej 1 element). W ciele pętli zdejmujemy na bieżąco każdy kolejny element (wstecz)
poprzez zastosowanie funkcji pop() z domyślnym - pustym - argumentem, po czym zwiększamy pierwszą literę
na dużą i odkładamy powstały w ten sposób string na kolejną listę - pierwotnie pustą - o nazwie let_in.
To odkładanie realizujemy dzięki funkcji append() która dodaje kolejny element na listę
"""
while waiting:
    name = waiting.pop()
    #print(waiting)
    name = name.title()
    print(f"Aktualnie na wejsciu oczekuje {name}")
    let_in.append(name)

print("\nWpuszczono: ") #iteracja polega na nadaniu nazwy iteratora w liscie i wydrukowanie iteatorem
for lt in let_in:
    print(lt, end="_")

print()

#wypisuje elementy poslugujac sie indeksami
for i in range(len(let_in)):
    print(let_in[i], end=" ")

print()
#wypisuje elementy posługując się tymczasową niedbałą zmienna iterującą w postaci podkreślnika
for _ in let_in:
    print(_, end="+")
print()

print(waiting)
print(let_in)

let_in.reverse()
print(let_in)
let_in.append("Kasia")
print(let_in)

first = let_in.remove("Kasia") #usuwa tylko pierwsze wystąpienie danego stringa
print(let_in)

