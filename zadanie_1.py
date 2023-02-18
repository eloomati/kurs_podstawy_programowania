users =['anna01', 'bob7', 'susan_lip']

while (u := input("Podaj uzytkownika")) != '':
    u = u.strip()
    if u not in users:
        print(f"{u}: zarejestruj sie!")
    else:
        print(f'Uzytkowniku {u}: przejdz do logowania')

print("Koniec")