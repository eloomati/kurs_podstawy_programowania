import random

from my_module import summa, sub, mult, div

print(summa(4, 5))

print(sub(4, 5))

print(mult(4, 5))

print(div(4, 5))

print(random.random()) #Wyrzuca losowe liczby od 0 do 1
print(random.randint(2, 99))

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a']
print(random.choice(lst))
random.shuffle(lst)
print(lst)