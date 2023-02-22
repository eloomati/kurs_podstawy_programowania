def celestial_objects(planet, distance):
    co = {'p': planet.title(), 'd': distance}
    return co

c1 = celestial_objects('earth', 1)
print(c1)

for k, v in c1.items():
    print(k, v)