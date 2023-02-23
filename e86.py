def components(prepared, used):
    while prepared:
        stuff = prepared.pop()
        print(f"Bierzemy {stuff}")
        used.append(stuff)

def show_used(used):
    print("Wykorzystane arytuły spożywcze:")
    for u in used:
        print(u)


prepared_t = ['masło', 'ser', 'szynka', 'papryka', 'pomidor', 'oliwki', 'rzodkiewka', 'cebula', 'sól', 'pieprz']
used_t = []

components(prepared_t, used_t)
show_used(used_t)

print(prepared_t)
print(used_t)