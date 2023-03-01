fname = 'plik1.txt'
file = open(fname)

try:
    lst = [row for row in file]


    for row in lst:
        print(row.rstrip())

finally:
    file.close()