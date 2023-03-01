# Zapisuje i nadpisuje tresc wskazanego pliku

fname = 'text.txt'

with open(fname, 'w') as f_ob:
    f_ob.write("Tekst zapisany ")