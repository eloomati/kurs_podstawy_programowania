#WYCINKI - wyjmowanie wycinka z listy
letters = ['a', 'v', 'c', 'b', 'r', 't', 'z']
print(letters[0:4])
print(letters[:4])
print(letters[3:])
print(letters[-2:])
print(letters[-2:0])#beez sensu bo wycinki dzialaja od lewej do prawej

for lett in letters[:4]:
    print(lett.upper(), end='')

str0 = "Hello Everybody"
print(str0[:-1])
print(str0[::-1]) #przed pierwszym dwukropkiem jest start, w srodku jest koniec, a na koncu krok
# Wypisujemy elementy od początku do końca tylko, że z krokiem -1, [start:stop:step]
# Start: od początku
# Stop: koniec bez tego elementu
# Step: krok, czyli co ile będziemy wypisywać

nums = [1, 2, 3, 4]
print(nums)
print(nums[:])
print(nums[::])
print(nums[::-1])