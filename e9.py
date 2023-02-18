num = .5
infinity = float('inf')
print(infinity, type(infinity)) #<-to jest liczba nie string

#liczby zespolone a+bi a rzeczywista, a b urojona
z = 2.3 + 5j #liczba urojona
print(z)
print(type(z))


#liczby sprzerzone
print(z.conjugate())

#wartosc boolowska
print(True, False)
print(type(True))

#dzielenie calkowite
print(9 / 2)
print(9 // 2)

#wartosc warta nic
number = None
print(number, type(number))

#modulo - reszta z dzielenia
print(9 % 4, 100 % 9)