import csv

# with open('RealFinalData2018.csv', 'r') as inp, open("placeholdervoorlijst.csv", 'w') as out:
#     lijst = []
#     next(inp)
#     for row in csv.reader(inp):
#         lijst.append(row[4])
#         lijst.append(row[5])
#     csv.writer(out).writerow(sorted(set(lijst)))

with open("nieuwere_sbk_postcode_buurtcombinatie.csv", 'r') as inp, open("placeholdervoorlijst.csv",'r') as inp2, open("placeholdervoorlijst2.csv",'w') as out:
    grotelijst= []
    minilijst = []
    eindpost = ''
    for row in csv.reader(inp):
        # print(row)
        beginpost = row[1]
        eindpost = row[2]
        words = csv.reader(inp2)
        for word in words:
            print(word)
        for member in words:
            minilijst.append(member)
            if member == eindpost:
                grotelijst.append(minilijst)
                minilijst = []
    csv.writer(out).writerow(grotelijst)
            
            