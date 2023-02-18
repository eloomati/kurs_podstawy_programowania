#tworzac obiekt przy pomocy copy niezaleznie od modyfikacji (czy gleboka czy nie) to bdziemy mieli niezalezny obiekt w pamieci
import copy

#w przypadku list zagniezdzonych, robimy takie zmiany przy uzyciu copy
# płytka kopia
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = copy.copy(l1)

print(l1)
print(l2)

l1.append([10, 11, 12])

print(l1)
print(l2)

print(id(l1))
print(id(l2))