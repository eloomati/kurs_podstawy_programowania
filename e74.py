nicks = {
    'susan1': [2, 3, 8],
    'john': [1, 12, 34],
    'terry': [23, 23, 98, 22],
    'luckas': [7]
}

# Wyjmowanie wartosci ze słownika zrobionego z list
for v in nicks.values():
   for i in v:
       print(i)

for nick, nums in nicks.items():
    print(f"\nLiczby uzytkownika {nick.upper()} to: ", end="")
    for n in nums:
        print(n, end=" ")