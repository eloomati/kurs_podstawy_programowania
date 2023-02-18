st = "\nPodaj kolory: "
st += "\nWpisz czarny aby zakonczyć."
text = ""

while text != "czarny":
    text = input(st)
    print(f"Wpisano: {text}")
else:
    print("Zakończono")
