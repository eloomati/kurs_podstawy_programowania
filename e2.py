#Konwersja i rzutowanie

num = '343'
print("Zmienna num:", type(num))
num = int(num)
print("Zmienna num:", type(num))

num1 = 12
print("Zmienna num1:", type(num1))
num1 = str(num1)
print("Zmienna num1:", type(num1))

num3 = 1.2975
print("Zmienna num3:", num3, type(num3))
num3 = int(num3)
print("Zmienna num3:", num3, type(num3))

num4 = 5
print("Zmienna num4:", num4, type(num4))
num4 = float(num4)
print("Zmienna num4:", num4, type(num4))

print(int(float('123.456')))