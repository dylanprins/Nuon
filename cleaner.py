import csv
with open('DataBase2017.csv', 'r') as inp, open('editDataBase2017.csv', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[8] != 'GAS':
            writer.writerow(row)