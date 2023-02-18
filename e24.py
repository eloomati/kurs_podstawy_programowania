"""
Pętla iteruje po tym długim stringu i jeżeli napotka po drodze spację (zrobiliśmy dlatego instrukcję warunkową
która jest odpowiedzialna za detekcję tej sytuacji), to wtedy wydrukuje zespół gwiazdek i natychmiast
przejdzie do następnego kroku pętli poprzez zastosowanie instrukcji continue, która omija
aktualny krok pętli (to co jest dalej) i przechodzi do następnego kroku pętli
"""


for s in "Dobry wieczór na programowanie w Pythonie!!":
    if s == " ":
        print("*****")
        continue
    print(s)

string = "Dobry wieczór na programowanie w Pythonie!!"
for s in string:
    if s == " ":
        print("*****")
        continue
    print(s)

"""
Pętla iteruje po tym długim stringu i jeżeli napotka po drodze spację (zrobiliśmy dlatego instrukcję warunkową
która jest odpowiedzialna za detekcję tej sytuacji), to wtedy wydrukuje zespół gwiazdek i natychmiast
przejdzie do następnego kroku pętli poprzez zastosowanie instrukcji continue, która omija
aktualny krok pętli (to co jest dalej) i przechodzi do następnego kroku pętli
"""

string = "Dobry wieczór na programowanie w Pythonie!!"
for s in string:
    if s == " ":
        print("*****")
        break
    print(s)