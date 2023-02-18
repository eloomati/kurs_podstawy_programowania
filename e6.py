word = "Bob O'Donell."
print(word)
word = 'Bob O"Dell'
print(word)
#word = 'Bob O'Donell' #->Błąd

word = 'Bob O\'Donell'
print(word)
word = "Bob O\"Donell" # -> \ to znak escapingu/ucieczki, nie traktuje znaków składniowych
print(word)

movie = 'Astronauta stwierdził: "Mój ulubiony ilm to A13."'
print(movie)
movie = 'Astronauta stwierdził: "Mój ulubiony ilm to \'A13\'."'
print(movie)
movie = "Astronauta stwierdził: 'Mój ulubiony ilm to \"A13\".'"
print(movie)
