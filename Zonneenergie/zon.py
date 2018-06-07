import csv
# lst = vind een lijst op 'https://maps.amsterdam.nl/_php/haal_objecten.php?TABEL=ZONNEPANELEN2015' '2015' in de url kan worden veranderd 
firstline = ['volgnr', 'lat', 'lon', 'label']
with open("zon2016.txt", "w") as out:
    writer = csv.writer(out)
    writer.writerow(firstline)
    for x in lst:
        line = []
        line.append(x['VOLGNR'])
        line.append(x['LATMAX'])
        line.append(x['LNGMAX'])
        line.append(x['LABEL'])
        writer.writerow(line)
with open('zon2016.txt') as inp, open("zon2016.csv", "w") as out:
    lines, mem = inp.readlines(), ''
    for line in lines:
        if line == '\n':
            line = line.replace("\n", "")
        mem += line
    out.write(mem)
    
    
