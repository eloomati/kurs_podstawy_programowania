def go_out(inp):
    if inp == "":
        return True

while True:
    a = input("Podaj pierwszą liczbę: ")
    if go_out(a): # Kończymy po naciśnięciu entera
        break

    b = input("Podaj drugą liczbę: ")
    if go_out(a):  # Kończymy po naciśnięciu entera
        break

    try:
        c = int(a) / int(b)
    except ZeroDivisionError:
        print(f"Nie można dzielić przez {b}")
    else:
        print(c)

print("Koniec")