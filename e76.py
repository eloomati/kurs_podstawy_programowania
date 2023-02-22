t1 = {'A': 97, "B": 14, "C": 34}
t2 = {'A': 197, "pi": 3.14, 'e': 2.71}
t1.update(t2) # Pernametnie aktualizuje slownik t1 slownikiem t2
print(t1)
# update zmienia nam na stale
t1 = {'A': 97, "B": 14, "C": 34}
t2 = {'A': 197, "pi": 3.14, 'e': 2.71}
print(t1 | t2) #Tymczasowo aktualizuje słownik t1 słownikiem t2
# | zmienia nam w locie, ale nie zmienia orginalnego slownika, to jest operator zlaczenia slownikow
print(t1)

t1 |= t2 # Pernametnie aktualizuje slownik t1 slownikiem t2 (tak samo jak metoda update)
print(t1)