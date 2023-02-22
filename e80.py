def tire(diameter, width):
    print(f"Opona: {diameter}, {width}")

tire(17, 225)
tire(16, 205)
tire(15, 215)
  #Argumenty pozycyjne
tire(diameter=17, width=225) # Argumenty nazweane (klucz = wartość)


def car(mark, model):
    mark = mark.title()
    print(f"Mój samochód to {mark}.")
    print(f"Posiadanym modelem marki {mark} jest {model.title()}")

car('honda', 'jazz')
car('jazz', 'honda')

car(model = 'civic', mark = 'honda')