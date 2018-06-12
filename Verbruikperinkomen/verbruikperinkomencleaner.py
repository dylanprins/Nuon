import csv
import pandas as pd

newrow = []
def appendinkomen(postcode):
    for line in inkomens:
        if line[0]==postcode[0:4]:
            moneys = line[2]
            newrow.append(postcode[0:4])
            newrow.append(oudverbruik)
            newrow.append(moneys)
            writer.writerow(line)
            newrow.clear()

with open('../DataBases/editDatabase2018.csv', 'r') as inp, open('witgewasseninkomen.csv', 'r') as sinp, open('verbruik per inkomen.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(['Postcode','Verbruik','Inkomen'])
    c=0
    oudverbruik = 0
    totaalverbruik=0
    length=0
    inkomens = csv.reader(sinp)
    numlines = len(pd.read_csv('../DataBases/editDatabase2018.csv'))
    newrow=[]



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
                if c == numlines+1:
                    sinp.seek(0)
                    appendinkomen(postcode)
                    c=0
                elif newpostcode[0:4] == postcode[0:4]:
                    nieuwverbruik=int(row[16])
                    oudverbruik = int(oudverbruik+nieuwverbruik)
                    postcode = row[4]
                else:
                    sinp.seek(0)
                    appendinkomen(postcode)
                    oudverbruik = int(row[16])
                    postcode = newpostcode



            