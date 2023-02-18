#liczby pierwsze - hipoteza rimana
from math import sqrt

n = 7
count = 0
for n in range(2, 100):
    is_prime = True
    s = int(sqrt(n))
    for i in range (2, s +1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} jest pierwsza.")
        count += 1

print(f"W tym przedziale jest {count}")