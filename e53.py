l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 'index']]
l2 = l1

l2[2][2] = 9
print(l1)
print(l2)

#zwroci to samo id co dowodzi temu ze mamy doczynienia z ta sama lista w pamięci
#to znaczy, że to PŁYTKA KOPIA  (SHALLOW COPY)
print(id(l1))
print(id(l2))