#nazwy kopii odnosza sie tylok donazwy funkcji z modulu copy, jesy .copy i .deepcopy, jest to roznica miedzy nimi
import copy

# Płytka kopia
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = copy.copy(l1)

l1[1][1] = 'SHALLOW'

print(l1)
print(l2)

print(id(l1))
print(id(l2))