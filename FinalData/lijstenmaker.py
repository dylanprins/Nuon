import csv

# with open('RealFinalData2018.csv', 'r') as inp, open("placeholdervoorlijst.csv", 'w') as out:
#     lijst = []
#     next(inp)
#     for row in csv.reader(inp):
#         lijst.append(row[4])
#         lijst.append(row[5])
#     csv.writer(out).writerow(sorted(set(lijst)))

with open("sbk_postcode_buurtcombinatie.csv", 'r') as inp, open("placeholdervoorlijst.csv",'r') as inp2, open("placeholdervoorlijst2.csv",'w') as out:
    grotelijst= []
    minilijst = []
    eindpost = ''
    next(inp)
    for row in csv.reader(inp):
        beginpost = row[1]
        eindpost = row[2]
        for word in csv.reader(inp2):
            for member in word:
                if member == eindpost: 
                    print(eindpost)
                    minilijst.append(member)
                    minilijst = []
                    break
                else:
                    minilijst.append(member)
            csv.writer(out).writerow(minilijst)
            break