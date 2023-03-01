name = 'plik1.txt'


with open(name) as f_ob:
    st = f_ob.readline() # czyta jedną linię z podanego pliku, bez wzgledu na podana illość argumentów

print(type(st)) # Klasa str

for s in st:
    print(s.rstrip())