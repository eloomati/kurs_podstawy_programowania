name = 'plik1.txt'


with open(name) as f_ob:
    st = f_ob.read(5) # Tworzy obiekt z klasy str a nie jak readline liste, dodatkowo read może przyjmować argumenty i odczytywać przez nas wybraną ilość

print(type(st)) # Klasa str

for s in st:
    print(s.rstrip()) # lub print(row, end='')