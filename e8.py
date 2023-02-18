#metoda encode i decode -> zamiana stringów na bajty

text = "Równanie płaszczyzny"
print(text)
print(len(text))
print(type(text))
print("--------------")
bytes = "Równanie płaszczyzny".encode('utf8') #string na bajty
print(len(bytes)) #czyli polske znaki rozmieszczone są na dwóch bajtach
print(type(bytes))
print(bytes) #wynik to zapis 16 77/16 = 4 a 13 to D wiec M to 4D
#77(10) = 4D(16)
print("--------------")
text = bytes.decode('utf8') #bajty na string
print(type(text))
print(text)
print("--------------")
cup = "☕"
emot = cup.encode('utf8')
print(len(emot))
print("Kawa "+str(emot)) #<- zajmuje 3 bajty
print("--------------")
smile = "😄"
emot = smile.encode("utf8")
print(len(emot))
print("Uśmiech: " + str(emot))
print("--------------")