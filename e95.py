x = lambda a, b: a + b
print(x(2, 8))

x = lambda a, b=1: a + b
print(x(2))

nums = [1, 2, 3, 4]
cubes = list(map(lambda x: x** 3, nums))
print(cubes)

print(list(filter(lambda a: a % 2, nums)))