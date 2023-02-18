from math import sqrt

#ZAD1
message = "KOMUNIKAT"
print(message)
#ZAD2
name = "Mati"
print(f"Witaj {name}")
#ZAD3
city = "sopot"
print(f"Male: {city.lower()}, duze {city.upper()}, z duzej: {city.title()}.")
#ZAD4
author = "Carl Fridrich Gauss"
print(f'{author} powiedział: "Jeśli matematyka jest królową nauk, to królową matematyki jest teoria liczb"')
#ZAD5
print('Mój ulubiony film to "Marsjanin"')
#ZAD6
print("Komputery\nInformatyka\nProgramowanie")
#ZAD7
print('Znajdujesz się\nna pokładzie "Międzynarodowej Stacji Kosmicznej"')
#ZAD8
a = "A"
b = "B"
c = "C"
d = "D"
print(a, b, c, d)
#ZAD9
name = "\t\tMateusz\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
#ZAD10
adj = "Duza"
verb = "leci"
print(f"{adj} satelita {verb}")
#ZAD11
x = 50
print(f"Dozwolona prędkość to " + str(x) +" km na godzinę. ")
#ZAD12
print(2+3)
print(7-2)
print(int(25/5))
print(5*1)
#ZAD13
atoms = 10 ** 80
print(atoms)
#ZAD14
x = 2
y = 7 * x ** 3 + 3 * x ** + 4 * x + 7
print(y)
#ZAD15
x = 1
y = 2
z = 3
sum = x + y + z
print(sum)
#ZAD16
python_dev = 5 * 15
java_dev = 2 * 20
sum = java_dev + python_dev
print(sum)
#ZAD17
x = 20
y = 5
comparison = x / y
print(f"Liczba x jest mniejsza od y o {comparison} razy.")
#ZAD18
bit = 10
bajt = 10
bit_converter = bajt / 8
bajt_converter = 8 * bit
print(f"{bit} bitów to {bajt_converter} bajtów, a {bajt} bajtów to {bit_converter} to bitów")
#ZAD19
m = 3
converter = m * (3600/1000)
print(int(converter))
#ZAD20
x = 10
y = 5
calc = x / y
calc_2 = x // y
print(calc, calc_2)
#ZAD21
x = 1
y = 2
averange = (x + y) / 2
print(averange)
#ZAD22
a = 1
b = 2
area = a * b
circuit = 2 * a + 2 * b
print(area, circuit)
#ZAD23
r = 5
l = 2 * 3.14 * r
p = 3.14 * r ** 2
print(l, p)
#ZAD24
a = 10
h = 4
area = a * h / 2
print(area)
#ZAD25
a = 4
b = 5
h = 3
p = ((a + b) * h) / 2
print(p)
#ZAD26
way = 10
time = 2
speed = way / time
print(f"Samochod przejechal {way} km w {time} godzin, jego srednia predkosc to {speed} km/h")
#ZAD27
km = 1
km_to_dm = km * 10
print(km_to_dm)
#ZAD28
x = 4
y = sqrt(x)
print(y)
#ZAD29
circuit = 360
hex = 16
alph = 26
hex_degree = circuit / hex
alph_degree = circuit / alph
diff = hex_degree - alph_degree
print(f"W systemie 16-ktowym kamera musi obracac się o: {hex_degree} stopni, przy alfabecie o {alph_degree} stopni, jest to różnica {diff} stopni")
#ZAD30
d = 1800
r = 900
l = 2 * 3.1415 * r
car_t =60 * ((l / 2 ) / 50_000)
elevator_t =60 * (d / 10_000)
diff = elevator_t / car_t
print(f"Obwód torusa to: {l}. Auto jedzie: {round(car_t, 3)} min, a winda {round(elevator_t, 3)}, więc auto jedzie {round(diff, 4)} razy szybciej")
#ZAD31
a = 1
b = 5
n = 3
s = ((a + b) / 2) * n
print(s)
#ZAD32
g = 8.91
my_q = 70 / g
m_g = 0.378 * g
j_g = 2.528 * g
m_my_q = my_q * m_g
j_my_q = my_q * j_g
print(my_q, m_my_q, j_my_q)
#ZAD33
dist = 5762.6
speed = 1000
calc = dist / speed

print(f"Podroz zajela {calc} godziny")
#ZAD34
dist = 2 * 2
v = 0.0033
calc = (dist / v)
calc_sec = calc / 60
calc_min = calc_sec / 60
print(f"Dzwiek od skaly oddanlonej o 2km wroci do nas po: {round(calc_sec, 2)} sekundach lub po: {round(calc_min,2)} min")
#ZAD35
v = 30_000
mars_distance = 78_000_000
neptun_distance = 4_300_000_000
mars_time = (mars_distance / v) / 24 / 30
neptun_time = (neptun_distance / v) / 24 / 365
print(f"Podróż na Marsa zajmie: {round(mars_time,3)} miesiecy, a na Neptuna {round(neptun_time, 3)} lat")
#ZAD36
light_speed = 300_000
distance = 4.24
calc = light_speed * distance
print(f"Najbliższa gwiazda do słońca leży w odległości {calc} km.")
