nums1 = {
    'prime': 2,
    'greater_than_100': False
}
nums2 = {
    'prime' : 31, 'greater_than_100': False
}
nums3 = {
    'prime': 2311, 'greater_than_100': True
}

primes = [nums1, nums2, nums3]
print(primes)

for prime in primes:
    print(prime)
print("---------------------")
for k, v in nums1.items(), nums2.items(), nums3.items():
    print(k)
    print(v)

for prime in primes:
    for k, v in prime.items():
        print(f"Klucz: {k}, watosc: {v}")