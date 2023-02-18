#formatowanie stringow e10-e12
from math import e

#SPECYFIKATORY ARGUMENTÓW (ZNAK %)
print(e)
print("Pierwsza cyfra %s E to %d. Liczba %f w notacji wykładniczej to: %e. " % ("liczby", 2, e, e))
# %s - string %d to liczba calkowita %f liczba float, zmiennoprzecinkowa %e notacja wykładnicza
# krotka to dwa nawiasy ()

#okreslanie dlugosci strina, uzupelnianie bialymi znakami
print("==%8s==" % ("Tekst")) #<- dopelnienie z lewej
print("==%-8s==" % ("Tekst")) # <- doppelnienie z prawej


print("==%16.5f==%-16.5f==" % (e,e))
print("==%16.5e==%-16.5e==" % (e,e))
print("==%20.2e==%-20.2e==" % (123.456789, 123.456789))

