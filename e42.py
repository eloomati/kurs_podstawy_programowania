robots = ['ramie', 'kontroler', 'gonsienica', 'silnik']

if 'silnik' in robots and 'kontroler' in robots and 'ramie' in robots:
    print("Montuje silnik!\nMontuje kontroler\nMontuje ramie")
    print('Asemblacja zakonczona')
else:
    print('\nBrakuje wszystskich niezbednych czesci')

print(robots[-1]) #indeksowanie od tylu


tools = ['lornetka', 'lupa', 'teleskop', 'sonda']
text = "Przedmiot obserwacyjny to "+ tools[-2] + "." #kontagenacja
print(text)
print(tools)
tools[0] = 'rakieta' #zamiana elemntów na liscie
print(tools)
tools[-2] = 'soczewka'
print(tools)

tools.append("spadochron") #to to samo
print(tools)
tools += ['sekstans'] #to to samo (rownowazne do append)
print(tools)