dc = {'A': 1, 'B': 2}

print(dc['A'])
print(dc.get('A'))

#print(dc['X'])
print(dc.get('X'))
print(dc.get('X', 'This key doesn\'t exist'))

dc = {}
print(type(dc))

coords = {}
print(coords)
coords['x'] = 7
coords['y'] = 67
print(coords)

dc0 = dict()
print(dc0)
dc1 = dict(x=0, g=2) #argument klucz wartosc
print(dc1)

dc2 = dict((('x', [3, 6, 7, 99]), ('y', 5), ('z', 9))) #argument pozycjyny
print(dc2)

del dc2['y'] #usuwa pozycje ze slownika pod odpowiednik kluczem
print(dc2)
dc2['v'] = 123
print(dc2)

kv = dc2.pop('v') #pozwala na wyjecie wartosci, usuniecie jej ze slownika i przypisania do nowej zmiennej
print(dc2)
print(kv)

print(list(dc2.keys()))
print(list(dc2.values()))
print(list(dc2.keys())[0]) #wypisuje nam klucz pod podanym indeksem

print('x' in dc2)
print('x' not in dc2)