import csv

fname = "cj_vancouver.csv"

with open(fname) as f_ob:
    rd = csv.reader(f_ob)
    header = next(rd)
    print(header)

    for index, header_element in enumerate(header):
        print(index, header_element)