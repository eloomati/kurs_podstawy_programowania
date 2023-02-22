def car(model, mark='honda'): #Gdy tworzymy parę klucz = wartość domyślna, to musi ona wystąpić na końcu listy paprametrów
    mark = mark.title()
    print(f"Mój samochód to {mark}.")
    print(f"Posiadanym modelem marki {mark} jest {model.title()}")

car(model='civic')
car(model='jazz')

car(model='swift', mark='suzuki')
car('swift', mark='suzuki')
car('swift', 'suzuki')

car('octavia', 'skoda')

car('r8')

# Poniższy kod spowoduje błąd
def fun(x, y, z):
    pass

fun(5, 7, x=2) # Przypisuje do x wartość dwa razy