disciplines = {}

flag = True

while flag:
    name = input("Podaj imie: ")
    disc = input("Podaj dyscypline: ").lower()

    disciplines[name] = disc

    next = input("Czy kontyuowac? ")
    if next == 'n':
        flag = False

for name, disc in disciplines.items():
    if disc == "astronomia":
        print(f"{name}: zakwalifikowales sie do pracy w obserwatorium")


if "astronomia" not in disciplines.values():
    print(f"Nikt nie aplikował w pracy w obserwatorium")