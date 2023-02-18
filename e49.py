tools = ['lornetka', 'lupa', 'teleskop', 'sonda']
tools.sort() #sortuje trwale

print(tools)

tools.sort(reverse=True)
print(tools)

lt = [(1, 4, 7), (4, 5, 1), (77, 2, 9 ), (2, 3, 5)]
lt.sort(key=lambda a: a[2])
# Zapis key = ... znaczy ze względu na co chce sortowac, tutaj: ze wzgledu na ostatni element
#każdej z krotk
print(lt)