engine = "start"
print(engine == "start")

engine = "stop"
print(engine == "start")

print(not 1, not 0, not 5, not not 0)

num0 = 15
num1 = 10
print(num0 >= 13 and num1 >= 13)
"""
Tablica prawdy dla koniunkcji logicznej (iloczynu logicznego)
1 and 1 = 1
1 and 0 = 0
0 and 1 = 0
0 and 0 = 0
"""

print(num0 >=15 or num1 > 10)
"""
Tablica prawdy dla alternatywy logicznej (sumy logicznej)
1 or 1 = 1
1 or 0 = 1
0 or 1 = 1
0 or 0 = 0
"""
is_equal = 4 == 4
print(is_equal)

my_number = 45
if my_number % 2 == 0:  # -> jeśli True
    print(f"Liczba{my_number} jest parzysta")
else: # -> jeśli False
    print(f"Liczba {my_number} jest nieparzysta")