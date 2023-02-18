#wprowadzanie liczby i sprawdzenie parzystości
inp = int(input("Podaj liczbę: "))
if inp % 2:
    print(f"{inp} jest nieparzysta")
else:
    print(f"{inp} jest parzysta")

    for i in range(1):
        print(f"Aktualnie wypisuje liczbę: {i}")
    print("------------------")
    lower_num = int(input("Podaj początek przedziału: "))
    higher_num = int(input("Podaj koniec przedziału: "))

    print("------------------")
    for i in range(lower_num, higher_num + 1):
        print(i)

    print("------------------")
    for i in range(10):
        print(i)

    print("------------------")
    for i in range(3, 10):
        print(i)

    print("------------------")
    for i in range(3, 50, 5):
        print(i)

    print("------------------")
    for i in range(100, 21, -2):
        print(i)