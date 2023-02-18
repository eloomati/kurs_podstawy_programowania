letter = input("Podaj litere: ")
i = 0
"""Program wypisuje po 5 razy litery az do momentu nacisniecia 
klawisza enter (while letter != '' """
while letter != "":
    print(letter)
    i += 1
    #Jezeli licznik (i) jest rowna 5, to wtedy zerujemy licznik bo chcemy liczyc nowa litere
    if i == 5:
        letter = input("Podaj kolejna: ")
        i = 0

print("bye bye!")
