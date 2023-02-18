noty = [3, 4.5, 18, 13, 5]
nota_min = noty[0]
nota_max = noty[0]

for n in noty:
    if n < nota_min:
        nota_min = n
    if n > nota_max:
        nota_max = n

print(noty, nota_min, nota_max)

for n in noty:
    if n == nota_min or n == nota_max:
        continue
    print(n)


"""
przyswoic skladnie, obejrzec przyklady, dodac nowe funkcjonalnosci
"""