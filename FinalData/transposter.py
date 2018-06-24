import csv
import operator
# with open('sbk_postcode_buurtcombinatie.csv', 'r') as inp, open('nieuwe_sbk_postcode_buurtcombinatie.csv', 'w') as out:
    # writer = csv.writer(out)
    # next(inp)
    # sortedlist = sorted(r, key=operator.itemgetter(1))
    # for row in csv.reader(inp):
    #     if row[1]
        
r=csv.reader(open("sbk_postcode_buurtcombinatie.csv"), delimiter=",")
next(r)
sortedlist = sorted(r, key=operator.itemgetter(1))

with open('nieuwe_sbk_postcode_buurtcombinatie.csv', 'w') as out:
    writer = csv.writer(out)
    for row in sortedlist:
        writer.writerow(row)

with open('nieuwe_sbk_postcode_buurtcombinatie.csv') as inp, open("nieuwere_sbk_postcode_buurtcombinatie.csv", "w") as out:
    lines, mem = inp.readlines(), ''
    for line in lines:
        if line == '\n':
            line = line.replace("\n", "")
        mem += line
    out.write(mem)