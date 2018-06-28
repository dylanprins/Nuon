import csv
with open('RealFinalData2009.csv', 'r') as inp, open('dd.csv', 'w') as geos:
    lst1 = []
    lst2 = []
    mem = ''
    for row in csv.reader(inp):
        lst1 += [row]
        print(lst1)
    for i in lst1:
        print("------------")
        mem += str(i[10:])[1:-1]
        mem += "\n"
    geos.write(mem)
    




# categories = lst1[0] + ['longitude', 'latitude']
# with open('Data2016.txt', 'w') as out:
#     writer = csv.writer(out)
#     writer.writerow(categories)
#     for i in lst1:
#         for j in lst2:
#             if i[5] == j[0]:
#                 i += [j[3]]
#                 i += [j[4]]
#                 if len(i) == 22:
#                     writer.writerow(i)
# with open('Data2016.txt') as inp, open("Data2016.csv", "w") as out:
#     lines, mem = inp.readlines(), ''
#     for line in lines:
#         if line == '\n':
#             line = line.replace("\n", "")
#         mem += line
#     out.write(mem)