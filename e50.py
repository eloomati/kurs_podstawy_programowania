import time

nums = list()
nums = list(range(1000))
nums = list(range(50, 101, 2)) #dzialaja wszystkie funkcje jak w range w instrukcji warunkowej
print(nums)

cubes = []
for i in range(1, 5):
    cb = i ** 3
    cubes.append(cb)
    print(cubes)
    time.sleep(1) #sekundowy odstep czasowy

print(cubes)