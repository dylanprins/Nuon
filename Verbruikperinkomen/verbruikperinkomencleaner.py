import csv
with open('../DataBases/editDatabase2018.csv', 'r') as inp, open('witgewasseninkomen.csv', 'r') as sinp, open('verbruik per inkomen.csv', 'w') as out:
    writer = csv.writer(out)
    c=0
    inkomens = csv.reader(sinp)
    for row in csv.reader(inp):
        postcode= row[4]
        if oudverbruik == 0:
            oudverbruik= row[16]
        if oudverbruik != 0:
            nieuwverbruik=row[16]
            totaalverbruik = oudverbruik+nieuwverbruik
        c+=1
        print(postcode)
        print(verbruik)
    for line in inkomens:
        postcodeinkomen= line[0]
        inkomen = line[2]