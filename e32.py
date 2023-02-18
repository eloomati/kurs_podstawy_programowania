num = 0

while num < 100:
    num += 1
    #w momencie napotkania liczby podzielnej przez 3 lub przez 5 omijamy jej wypisywanie (printa)
    #przechodzac dzieki conitue do nastepnego kroku petli
    if num % 3 == 0 or num % 5 == 0:
        continue
    print(num)