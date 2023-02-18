var1 = -5
var2 = 3
var3 = 9
"""
Poniższa intrukcja warunkowa bada czy w zmianenej va1 i var2 są wartości dające wynik treu,
natomiast ostatnia składowa to rzeczywisty warunek stwierdzający, czy var 3 jest wieksze od zera. 
Dla danych, które znajdują się w zmiennej powyżej, instrukcja warunkowa sprawdzi więc,
czy var1 to true (Każda liczba inna od 0 jest true),
czy var2 > 0 i czy var3 jest większe od zera, Tutaj wszystkie 
trzy skłądowe dadzą w efekcie wynik Treu i zostanie wyświetlony napis OK

"""
if var1 and var2 and var3 > 0:
    print("OK")

if var1 > 0 and var3 >0 and var3 > 0:
    print("Wszystko większe od 0")