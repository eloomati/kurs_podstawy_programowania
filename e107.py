#Ta metoda jest najbardziej polecana do otwirania plików bo with dodatkowo dba o to żeby zamykać plik po
name = 'plik1.txt'

"""
Uzycie bloku with w przeciwienstwie do poprzedniego programu powoduje automatyczne
zamkniecie pliku bez wyciekow pamieci, poprzez niejawne zastosowanie funkcji close().
W tym przykladzie funkcja readlines() wczytuje wszystkie wiersze pliku, ktore mozemy dodatkowo
umiescic na liscie dostepnej po wyjsciu z bloku with
"""

with open(name) as f_ob:
    rows = f_ob.readlines() # Zczytuje wszystkie wiersze  i tworzy z nich listę dodając jeszcze biał znaki

print(type(rows))

for row in rows:
    print(row.rstrip()) # lub print(row, end='')