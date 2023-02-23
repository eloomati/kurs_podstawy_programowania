def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

lst = list(range(2, 1000))
print(list(filter(prime, lst)))


def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5)+ 1, 2):
        if n % i == 0:
            return False
    return True

natural_num = list(range(0, 1000))
print(len(list(filter(is_prime, natural_num))))