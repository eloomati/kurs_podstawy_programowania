import copy

# Głęboka kopia
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = copy.deepcopy(l1)

l1[1][1] = 'DEEPCOPY'

print(l1)
print(l2)

print(id(l1))
print(id(l2))
marks