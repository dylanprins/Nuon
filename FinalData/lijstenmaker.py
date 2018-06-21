import csv

with open('RealFinalData2018.csv', 'r') as inp:
    lijst = []
    next(inp)
    for row in csv.reader(inp):
        lijst.append(row[4])
        lijst.append(row[5])

    print(sorted(set(lijst)))

with open("sbk_postcode_buurtcombinatie.csv", 'r') as inp2:
    grotelijst= []
    csv.reader(inp)
