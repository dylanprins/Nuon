import csv
#with open('DataBase2018.csv', 'r') as bestand:
#    reader = csv.reader(bestand)
#    for row in reader:
#        for data in row:
#            if data == 'GAS':
#                writer.writerow(row)
with open('DataBase2016.csv', 'r') as inp, open('editDataBase2016.csv', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[8] != 'GAS':
            writer.writerow(row)