tools = ['lornetka', 'lupa', 'teleskop', 'sonda']
"""
Funkcja insert() wstawia dany element pod określony indeks i wymaga podania dwóch argumentów
Z kolei instrukcja del usuwa element spod określonego indeksu
"""

tools.insert(0, "łazik") #wymaga indeksu i przedmiotu (indeks, przedmiot)
print(tools)
del tools[3]
print(tools)

l1 = [2, 3, 4, 5]
l2 = ['a', 'b', 'c']
print(l1 + l2) #robi w locie
print(l1)

l1 += l2 # robi pernamentinie

print(l1 * 10) #multiplikuje liste, powtarza elemnty tak duzo ile ja mnozymy

