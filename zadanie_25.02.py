import random

while True:
    if exit == 'n': break
    inp_min = int(input("Podaj liczbę A: "))
    inp_max = int(input("Podaj liczbę B: "))
    lst = list(range(inp_min, inp_max))
    x = random.choice(lst)
    print(x)


    while True:
        print(f"Mamy przedział od {inp_min} do {inp_max}")

        inp = int(input("Zgadnij co wylosowałem: "))

        if x == inp:
            print("Zgadłeś!")
            break
        elif x < inp:
            print(f"Podałeś: {inp}... to za dużo!")
            continue
        elif x > inp:
            print(f"Podałeś: {inp}... to za mało :(")

    exit = input("Czy chcesz zgadywać jeszcze raz? Y/n")




