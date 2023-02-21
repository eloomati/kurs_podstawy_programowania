stuff = ['ksiazka', 'obraz', 'ramka', 'figura', 'plakat', 'doniczka']

if stuff: #sprawdza czy ma elementy na liscie if len(stuff) > 0
    for s in stuff:
        print(f"Umieszczam na polce {s}")
    print("Zrobione")
else:
    print("Nie mam co polożyć na półce")


robot = ['ramie', 'silnik', 'kontroler', 'gasienica', 'kolo', 'bateirie', 'łąńcuch']
parts = ['sterownik', 'kolo', 'przycisk', 'port usb']

for p in parts:
    if p in robot:
        print(f"Bingo, czesc {p} jest juz zamotowana")
    else:
        print(f"Montuje {p}")

print("\nAsemblacja zakonczona")