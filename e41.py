engineers = ['fabian', 'daniel', 'maria']
eng = 'jola'

if eng not in engineers:
    print(f"{eng.title()} przejdz do lab0")
else:
    print(f"{eng.title()} przejdz do lab5")

users =['anna01', 'bob7', 'susan_lip']
u = input('Podaj użytkowniak: ')

while u != '':
    if u not in users:
        print(f"{u}: zarejestruj sie!")
    else:
        print(f'Uzytkowniku {u}: przejdz do logowania')
    u = input("Podaj uzytkownika")

print("Koniec")

while u := input("Podaj uzytkownika"):
    if u not in users:
        print(f"{u}: zarejestruj sie!")
    else:
        print(f'Uzytkowniku {u}: przejdz do logowania')

print("Koniec")