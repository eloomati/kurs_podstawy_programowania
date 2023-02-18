# udowodnienie, że rzeczywiście obie listy są tymi samymi obiektami w pamięci bo zwracają też to samo id
# (oprócz tego, że appendowanie obu z nich doprowadza do dodania elementów na obu tych listach)
#PŁYTKA KOPIA

vehicles1 = ['samochod', 'motocykl', 'rower', 'hulajnoga']
vehicles2 = vehicles1

vehicles1.append('deskorolka')
vehicles2.append('quad')

print(vehicles1)
print(vehicles2)

print(id(vehicles1))
print(id(vehicles2))