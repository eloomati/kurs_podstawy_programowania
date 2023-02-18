#Instrukcje warunkowe e15-e21
age = 19
if age > 18:
    print("Jesteś dorosły")
    print("Masz 18 lat lub więcej")

number = 77

if number == 7:
    print(f"Liczba {number}.")
else:
    print(f"Nie wprowadziłeś 7, tylko {number}.")

day = 1
if day == 5 or day == 6 or day ==7:
    print("Weekend")
else:
    print("Uczymy się!")

if day >= 5 and day <= 7:
    print("Weekend")
elif day >= 1 and day < 5:
    print("Uczymy się...")
    weekend = 5
    x = 5 - day
    print(f"do weekendu zostało:{x}!")
else:
    print("Dane są niepoprawne")