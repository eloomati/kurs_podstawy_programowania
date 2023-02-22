nums = {
    "dave": 3,
    'albert': 1,
    'michal': 3,
    'tomek': 5,
    'dave': 9,
    'jim': 5
}
# Nie może być dwóch takich samych kluczy w słowniku. W przeciwnym przypadku pierwszy klucz zostanie zastąpiony drugim
# Nie tworzymy dwóch takich samych kluczy (błąd semantyczny, a nie syntaktyczny)
print(nums)

# Iterując po zduplikowanych kluczach automatycznie usuwa te duplikaty (można w tym celu jawnie użyć metody set)
for k in nums.keys():
    print(k, end=' ')

print()
for v in nums.values():
    print(v, end='')

print()
# Dzięki metodzie set usuwam duplikaty wartości
for v in set(nums.values()):
    print(v, end='')