#GLEBOKA KOPIA


vehicles1 = ['samochod', 'motocykl', 'rower', 'hulajnoga']
vehicles2 = vehicles1[:] #[:] <-- to wycinek, dodajac go towrzymy gleboka kopie

vehicles1.append('deskorolka')
vehicles2.append('quad')

print(vehicles1)
print(vehicles2)

print(id(vehicles1))
print(id(vehicles2))