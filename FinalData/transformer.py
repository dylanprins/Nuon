import csv
with open('Data2010.csv', 'r') as inp, open('editDataBaser2018.csv', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        try:
            row[11] = float(row[11])/100
            row[12] = float(row[12])/100
            row[13] = float(row[13])/100 
            row[14] = float(row[14])/100 
            row[17] = float(row[17])/100 
            row[18] = float(row[18])/100
        except ValueError:
            writer.writerow(row)
            continue   
        writer.writerow(row) 
    
with open('editDataBaser2018.csv') as inp, open("RealFinalData2010.csv", "w") as out:
    lines, mem = inp.readlines(), ''
    for line in lines:
        if line == '\n':
            line = line.replace("\n", "")
        mem += line
    out.write(mem)