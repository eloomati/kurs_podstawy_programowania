#operator ternarny - skrocona instrukcja warunkowa
a = "Pole" if True else "Obwód"
print(a)

a = "Pole" if False else "Obwód"
print(a)

a = "Pole" if 2 > 5 else "Obwód"
print(a)

"""
Operator ternarny (trójargumentowy) jest skróconą wersją instrukcji warunkowej
Jeżeli warunek zwróci wartość True, to wtedy "pójdzie" na lewo i wyświetli Pole
w przeciwnym przypadku pójdzie na prawo (do else'a) wyświetlając frazę Obwód

Używamy go żeby sprawdzić coś na szybko, przy najłatwiejszych sytuacjach
"""