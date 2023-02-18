i = 0
x = 40
expression = 5 * x * i + 1

while expression < 1000:
    print(f"{i}: {expression}")
    i += 1
    expression = 5 * x * i + 1

i = 0
x = 40
while (expression := 5 * x * i +1) < 1000:
    print(i, expression)
    i += 1