temp = 120

if temp < 0:
    water = "lód"
elif temp < 100:
    water = "ciecz"
else:
    water = "gaz"

print(f"Przy temperaturze {temp} st. C, stan skupienia wody to {water}")

day = 6
if day == 1:
    print("PN")
elif day == 2:
    print("WT")
elif day == 3:
    print("ŚR")
elif day == 4:
    print("CZW")
elif day == 5:
    print("PT")
elif day == 6 or day == 7:
    print("Trochę przerwy")
else:
    print("Nieprawidłowe dane")