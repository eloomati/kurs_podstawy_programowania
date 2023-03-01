fname = "plik1.txt"

with open(fname) as f_ob:
    for row in f_ob:
        print(row)

with open(fname) as f_ob:
    print([row for row in f_ob])

with open('plik1.txt') as f_ob:
    all = f_ob.read()
    print(all)

absolute_path = "C:\\Users\\hetko\\PycharmProjects\\pythonProject\\plik1.txt"

with open(absolute_path) as f_ob:
    all = f_ob.read()

print(all)
print(f"Ilość znaków w pliku: {len(all)}")