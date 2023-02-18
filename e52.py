#pozwala zarzadzac pamiecia w zapisywaniu

a = 7
b = a
a = 8
print(a, b)

# PŁYTKA KOPIA (SHALLOW COPY), tzn. że zmieniając listę pochodną zmieni mi się także lista źródłowa
a = [1, 2, 3, 4]
b = a
b[0] = 'word'
print(a, id(a)) # --> id() zwróci identyfikator obiektu w pamięci a dla płytkiej kopii te ident. będą równe
print(b, id(b))

# GŁEBOKA KOPIA (DEEP COPY), tzn. że zmieniając listę pochodną NIE zmieni mi się lista źródłowa a TYLKO ta pochodna
a = [1, 2, 3, 4]
b = a[:]
b[0] = 'word'
print(a, id(a)) # --> id() zwróci identyfikator obiektu w pamięci a dla głębokiej kopii te ident. będą różne
print(b, id(b))