'''
Funkcja zawiera 2 parametry: jeden pozycyjny, a drugi w postaci operatora rozpakowywania sekwencji
czyli gwiazdki (co defacto oznacza utworzenie w Pythonie krotki elementów, po której można iterować)
'''

def chars(num, *letters):
    for lett in letters:
        print(num, lett)
        print(num + 1, lett)

chars('a')
chars(5, 'a')
chars(2, 'a', "e", "c", "word", [1, 2, 3, 4])
chars(9, 'a', "e", "c", "word", [1, 2, 3, 4])