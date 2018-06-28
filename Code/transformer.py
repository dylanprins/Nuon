import csv
with open('Data2016.csv', 'r') as inp, open('RealFinalData2016.csv', 'w') as out:
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
    
