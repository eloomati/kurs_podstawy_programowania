import copy

# Głeboka kopia
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = copy.deepcopy(l1)

print(l1)
print(l2)

l1.append([10, 11, 12])

print(l1)
print(l2)

print(id(l1))
print(id(l2))