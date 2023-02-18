#METODA FORMAT
print("{0} {2} {cialo} {1}{3}".format('Misja Artemis', 2022, 1, '.', cialo='na księżyc w roku'))

print("Część rzeczywista: {0.real}, część urojona: {0.imag}".format(3.2j ** .28))

print("Pierwsza liczba: {0}, druba liczba: {1}".format(35,23))

#na koncu w formule format na koniec daje sie slowniki i listy
string = "Planeta: {planety[2]}; odleglość od słońca: {odleglosci[Ziemia]} {0}{1}"
print(string.format("mln km", ".", planety=["Merkury", "Wenus", "Ziemia", "Mars"],
    odleglosci ={
    'Merkury': 70.34,
    'Wenus': 101.3,
    'Ziemia': 149.6,
    'Mars': 230.3
}))

string = "Planeta: {planety[3]}; odleglość od słońca: {odleglosci[Mars]} {0}{1}"
print(string.format("mln km", ".", planety=["Merkury", "Wenus", "Ziemia", "Mars"],
    odleglosci ={
    'Merkury': 70.34,
    'Wenus': 101.3,
    'Ziemia': 149.6,
    'Mars': 230.3
}))

#formatowanie formatu :P
string = "{0:@>15s}|{1:_<15s}|{0:.^10s}" #>uzupelnia do lewej < uzpelnia do prawej ^uzupelnia na srodku
print(string.format('Język', 'Python'))

string="|{0:@>25.5f}|{1:*^25.5e}|"
print(string.format(2.123123123213, 5.213123143513413413413213213))