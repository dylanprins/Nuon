import csv
with open('Inkomen.csv', 'r') as inp, open('witgewasseninkomen.csv', 'w') as out:
    writer = csv.writer(out)
    c = 0
    for row in csv.reader(inp):
        newrow = []
        if c == 0:
            newrow.append(row[0])
            newrow.append(row[1])
            newrow.append(row[2])
            c+=1
        elif c==1 and row[1] != '0' and row[1] !='100':
            newrow.append(row[0])
            newrow.append(row[1])
            newrow.append(row[3])
        if (len(newrow)) != 0:
            writer.writerow(newrow)
