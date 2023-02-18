# tablica jest zwartym elementem w jednym miejscu, lista ma rozrzucona pamiec i mozna ja edytowac co znaczy dodawac nowe elementy
# lity moga przechowaywac slowniki i inne listy, posiadaja komorki, jak szafki z szufladami. Zmienna ma jedna wartosc, a na liscie
#mozna umiescic wiele wartosci. Listy sa zbiorami zmiennych. Indeksowanie od 0 do n-1 ( indeks to numer komorki gdzie znajduje sie elemenet)
# dynamiczne struktury danych i mozna zmieniac ich zawartosc, mozna dodawac, usuwac, edytowac elementy

#TABLICE e40 -
nums = [-3, 7, 8, 9, -12.4]
print(type(nums))
color1 = 'green'
colors = ['bialy','czarny', 'zielony', color1]
mix = ['naprawa','4', 'olej', 1.0, 2000]
print(len(mix))

tools = ['lornetka', 'lupa', 'teleskop, sonda']
print(tools)
print(tools[0])
print(tools[0].title())
print(len(tools[0]))

lst0 = [0, 1, 2, 3, 4]
lst1 = ["a", "b", "c"]
lst2 = ["klucz", "sruba", "srubokret"]
res = [lst0, lst1, lst2]
print(res)
print(res[1][1])
print(res[2][2])
print(res[1][0])
print(res[3]) # Bład przekroczenia zakresu listy

print('klucz' not in lst1, 'klucz' in lst2)

