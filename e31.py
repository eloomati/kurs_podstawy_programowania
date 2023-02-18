st = '\n Podaj imie:'
st += "\n(Wpisz 'q', aby zakończyć)"

while True:
    name = input(st)

    if name == 'q':
        break

    print(f"Wpisane imie: {name.title()}")