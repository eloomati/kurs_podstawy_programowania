#Slownik - struktura danych ktora sklada sie z klucz wartosc
rocket = { 'name': 'SLS', 'weight': 2000}
print(rocket['name'])
print(rocket['weight'])
# Słownik to struktura danych składająca się z par klucz-wartość
# aby wypisać wartość słownika należy posłużyć się kluczem
# na przykład rocket["name"] wypisze wartość w postaci SLS
#slowniki sa mutowalne
#listy i slowniki nie moga byc kluczami
#Wsrtoscia moze byc wszystko, wlacznie z innym slownikiem
print(rocket)


var = 34
dt = {
    (1, 2, 3): ['a', 'b', 'c'],
    3.14: "pi",
    "e": 2.71,
    "e": 2,
    1: "zero",
    var: 'text'
}

print(dt)
print(dt[(1, 2, 3)], dt[3.14], dt["e"], dt[1], dt[var])