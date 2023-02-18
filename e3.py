# Konkatenacja - łączenie elementów ze znakiem plusa
# Jeżeli używamy plusa do konkatenacji to musimy zamienić zmienne na stringa

from_sun = 3
text = "Ziemia jest " + str(from_sun) + " planeta od Słońca"
print(text)

name = 'jon littlewood'
print(name.title())
print(name.upper())

name1 = "Freeman Dyson".upper()
print(name1)
print(name1.lower().title())

phrase = "Matematycy: " + name.title() + ", " + name1.title() + "."
print(phrase)

res = 5000
txt = "Mamy "
print(txt + " " + str(res) + " bucksów $$$")

