import csv
with open('Data2010.csv', 'r') as inp, open('editDataBaser2018.csv', 'w') as out:
    writer = csv.writer(out)
    