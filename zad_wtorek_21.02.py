#Za pomocą listy składanej wygeneruj liczby podzielne przez 5 w zakresie od 1 do 100 i
#zsumuj je

suma = 0
nums = [i for i in range(0, 101) if i % 5 == 0]
print(nums)
for i in nums:
    suma += i
print(suma)

print(sum(nums))

s = 0
print([s := s + i for i in range(1, 101) if i % 5 == 0][-1])