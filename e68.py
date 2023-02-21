client78 = {
    'login': 'dnowak',
    'first_name': 'daniel',
    'last_name': 'nowak',
    'nick': 'nowak',
    'basket': 0
}

for k, v in client78.items():
    print(f"Klucz {k}, wartość {v}", end="")
print()
for k in client78.keys():
    print(f"Klucz {k}", end="")
print()
for v in client78.values():
    print(f"Wartosc {v} ", end="")
print()
for k in client78:
    print(k, end="")

#Iteracja po kluczu jst domyslnym dzialaniem pythona