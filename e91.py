from math import sqrt, log2, log, log10

print(abs(-1))
print(bool(0), bool(1))
print(dir(['tekst', 'listy'])) #wyswietla metody ktore mozna zastosowac na argumencie
print(dir(5))
#help(str)
nums = [1, 2, -9, 0 , 33, 12, 111, 7]
print(max(nums), min(nums))

letters = ['a', 'z', 'k', 'A', 'Z', 'K']
print(min(letters), max(letters))

nums = [4, 1, 2, 41, 4, 13]
print(min(nums, key=sqrt))  # Zwróci 1 bo sqrt(1) jest najmniejszym pierwiastkiem z liczb listy
print(max(nums, key=sqrt))  # Zwróci 41 bo sqrt(41) jest największym pierwiastkiem z liczb listy

print(sum(nums))
print(sum([[-1, -11], [-111, -1111]], [100]))
# Tutaj funkcja sum() tak naprawdę łączy listy, ale muszę mieć 2 parametr tej funkcji w postaci jakiejś listy (może być pusta)
nums = list(range(0, 42, 3))
print(nums)
print(sum(nums))

print(log2(1024), log(256), log10(1000))

message = "Jeden z kanałów RGB to zielony."
print(message.replace('zielony', 'niebieski'))
print(message)

print("kotkotkot".replace('t', 'd', 2))

txt = "Dzis mamy czwartek i programujemy wieczorem w Pythonie"
print(txt.split())
print(txt.split('i', 2))
print(txt.rsplit("i", 2))

print(" ".join(['Szła', 'dzieweczka', 'do', 'laseczka']))
print("Szła dzieweczka do laseczka".startswith("Szła"))
print("Szła dzieweczka do lasezka".endswith("laseczka"))
txt = 'tekst17'
print(txt.isalpha(), txt.isdigit(), txt.isalnum()) #isalnum() sprawdza czy w ciągu są znaki alfanumeryczne (alfabet, cyfry

print(ord('A')) #Zamieniam sobie na kod aski
print(chr(65))