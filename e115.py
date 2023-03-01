a = 5
b = 7
c = 0

try:
    print(a)
    y = a / c
except: # Wywołanie nie określonego nigdzie wyżej wyjątku
    y = b / c #Wyjątek w obsłudze wyjątku
finally: # Ratuje sytuacje, bo chociaż finally coś wyświetli
    print("Przechwycono wyątek wyjątku")