fname = "asdadsa.txt"

try:
    with open(fname) as f_ob:
        all = f_ob.read()
except FileNotFoundError:
    print("Nie znaleziono pliku")