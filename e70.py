disciplines = {}

flag = True

while flag:
    name = input("Podaj imie: ")
    disc = input("Podaj dyscypline: ")

    disciplines[name] = disc

    next = input("Czy kontyuowac? ")
    if next == 'n':
        flag = False

for name, disc in disciplines.items():
    if disc == "Astronomia".lower():
        print(f"{name}: zakwalifikowales sie do pracy w obserwatorium")


if "Astronomia".lower() not in disciplines.values():
    print(f"Nikt nie aplikował w pracy w obserwatorium")