#lista skladana - ma specyficzny sposob odkladania elemnetow, robi sie to szybko
nums = []
for i in range(20):
    nums.append(i)

print(nums)



#Ekwiwalent powyższego - lista składana (list comprehension)
nums = [i for i in range(20)]
print(nums)

cubes = [i ** 3 for i in range(20)]
print(cubes)

chars = [s for s in "Dzisiaj jest wtorek, a więc programujemy w Pythonie"]
print(chars)

sequence = list(range(10))
power = [i ** 4 for i in sequence if i % 3 == 0] #instrukcja warunkowa uzywana na liscie skladanej
print(power)

powers = [[i, i **1, i **3] for i in range(1,73)]
print(powers)

arr = [[0 for i in range(8)]for i in range(8)]
for a in arr:
    print(a)
print(arr)

#lista musi miec nadana nazwe, przyoisujmy do niej nawiasy i w nich zaczynam odkladac elementy na liscie
#czyli mam petle (tutaj for) ona dziala na liczbach wyznaczonych w swoich nawiasach
#iterujac po petli chcemy zeby liczby odlozyly sie na liste