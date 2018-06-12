import csv
with open('../DataBases/editDatabase2018.csv', 'r') as inp, open('witgewasseninkomen.csv', 'r') as sinp, open('verbruik per inkomen.csv', 'w') as out:
    writer = csv.writer(out)
    c=0
    oudverbruik = 0
    totaalverbruik=0
    inkomens = csv.reader(sinp)
    for row in csv.reader(inp):
        if c==0:
            c+=1
        elif c==1:
            if oudverbruik == 0:
                oudverbruik= row[16]
                print(oudverbruik)
                postcode=row[4]   
            if oudverbruik != 0:
                newpostcode=row[4]
                if newpostcode[0:4] == postcode[0:4]:
                    nieuwverbruik=row[16]
                    totaalverbruik = oudverbruik+nieuwverbruik
                    postcode = row[4]
                else:
                    totaalverbruik = 0
                    oudverbruik = 0

    for line in inkomens:
        postcodeinkomen= line[0]
        inkomen = line[2]