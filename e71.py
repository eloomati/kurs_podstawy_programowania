colors = {
    'blue' : 'niebieski',
    'green': "zielony",
    'black': 'czarny',
    'pink': 'różowy',
    'yellow': 'żółty',
    'brown': 'czerwony',
    'red': 'czerwony',
    'orange': 'pomarańczowy',
    'white': 'biały',
    'purple': 'fioletowy'
}

while True:
    what_lang = input("Jakie tłumaczenie (ang-pl - 1, pl-and - 2) ")

    if what_lang != "1" and what_lang != "2":
        print("Wprowadz 1 albo 2")
        continue

    what_color = input("Jaki kolor Cię interesuje: ").lower().strip()

    if what_lang == '1':
        for k, v in colors.items():
            if k == what_color:
                print(f"Po polsku: {v}")
                break
    else:
        for k, v in colors.items():
            if v == what_color:
                print(f"Po angielsku: {k}")
                break

    next = input("Kontynuować? (t/n) ")
    if next == "n":
        break