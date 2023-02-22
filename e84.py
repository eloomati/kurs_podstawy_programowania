def warehouse(name, quantity):
    all = name + "(" + quantity + ")"
    return all

def go_out(s):
    if s == '':
        return True

dt = {} #nowy slownik do wypelnienia

while True:
    print('Naciśnij "Enter", aby zakończyć wprowadzanie produktów')
    get_name = input("Nazwa: ")
    get_quantity = int(input("Ilość: "))

    if go_out(get_name) or go_out(get_quantity):
        print("Nie podano jednej z wymaganych charakterystyk")
        break

    dt[get_name] = get_quantity # Tutaj zapelniamy slownik
    data = warehouse(get_name, get_quantity)
    print(f"\nStan: {data}")

print(dt)