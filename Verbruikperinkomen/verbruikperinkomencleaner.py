import csv
with open('../DataBases/editDatabase2018.csv', 'r') as inp, open('witgewasseninkomen.csv', 'r') as sinp, open('verbruik per inkomen.csv', 'w') as out:
    writer = csv.writer(out)
    c=0
    oudverbruik = 0
    totaalverbruik=0
    length=0
    inkomens = csv.reader(sinp)
    numlines = len(inp.readlines())
    print(numlines)
    for row in csv.reader(inp):
        if c==0:
            c+=1
        elif c!=0:
            c+=1
            if oudverbruik == 0:
                oudverbruik= int(row[16])
                postcode=row[4]   
            if oudverbruik != 0:
                newpostcode=row[4]
                if newpostcode[0:4] == postcode[0:4]:
                    nieuwverbruik=int(row[16])
                    oudverbruik = int(oudverbruik+nieuwverbruik)
                    postcode = row[4]
                else:
                    print(oudverbruik)
                    oudverbruik = int(row[16])
                    postcode = newpostcode
    print(c)
    for line in inkomens:
        postcodeinkomen= line[0]
        inkomen = line[2]