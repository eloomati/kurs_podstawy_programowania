#KROTKI - są niezmienialne

coords = (200, 50) #krotka (tupla, ang. tuple
print(coords[0])

#coords[0] = 100 # Zwróci Traceback, ponieważ krotki są niemutowalne (immutable), tzn. nie można ich zmieniać

for c in coords:
    print(c)

coords = (12, 113) #Mozemy podmieniac nazwy krotek i na to nam python pozwala

#uzywamy ich o tego zeby miec penosc ze dane nie zostana nigdy zmienione