def get_data(number, discipline, **info):
    table = {}
    # informacje wstępne pobirane z argumentów pozycyjnych (number, discipline)
    table['nr'] = number
    table['dsc'] = discipline

    for key, value in info.items():
        table[key] = value

    return table

summary1 = get_data(23, 'Basketball',
         team="Chicago Bulls", name="Micheal", surname="Jordan", height=1.98, weight=100,
         age=50, country="USA", salary=100_000)

print(summary1)
for k, v in summary1.items():
    print(k, v)

summary2 = get_data(9, 'Soccer',
                    team="FC Barcelona", name="Robert", surname="Lewansowski", height="1.85", weight=80,
                    age=34, country="Poland", salary=1_000_000)

print(summary2)
for k, v in summary2.items():
    print(k, v)

summary3 = get_data(7,'Tennis',
                    name='Iga', surname='Świątek', height=1.76, weight=65,
                    age=21, country='Poland', salary=1_000_000)

print(summary3)
for k, v in summary3.items():
    print(k, v)