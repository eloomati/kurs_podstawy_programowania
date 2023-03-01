fname = 'plik1.txt'
file = open(fname)
print(type(file))

lst = [row for row in file]
print(lst)

for row in lst:
    print(row.rstrip())

print(lst[2][1])
print(lst[0][3]) # Wypisuje znak nowego wierasza
#print(lst[0][4]) # Wyrzuca błąd bo pierwszy element listy ma 4 elementy