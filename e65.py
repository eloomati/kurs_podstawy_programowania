#zbiory

odd = set([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])
primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23])
print(type(odd))

print(odd | primes) #sumuje nam zbiory
print(odd & primes)#czesc wspolna, iloczyn zbiorow, przeeciecie wzorow
print(odd - primes) #roznica lewostronna miedzy zbiorami, wyświetli to czego nie ma w zbiorze primes
print(primes - odd) # Różnica prawostronna: wyświetli to czego nie ma w zbiorze odd

#MOżna przekształcić odwrotnie, tzn. zbiór na listę
lst = list(set([1, 2, 3]))
print(lst, type(lst))

# nie moze posiadac duplikaów, żaden element nie może się powtarzać, każda dana jest unikatowa
s = set([1 , 2, 3, 3, 5, 6, 8, 3])
print(s)


#W secie moze byc krotka lub lista
s1 = set((1, 2, 2, 3))
print(s1)

t1 = tuple(set([1, 2, 3, 2, 2])) #Zamieniamy liste na set i set na krotke
print(t1)

s2 = {1, 2, 3, 5, 5, 6, 5, 8} # To jest zbior czyli set, deklarujemy go {} nawiasami
print(type(s2))