import csv
import pandas as pd
import bokeh
from bokeh.plotting import figure, output_file, show
import numpy as np
data09 = pd.read_csv("RealFinalData2009.csv")
data10 = pd.read_csv("RealFinalData2010.csv")
data11 = pd.read_csv("RealFinalData2011.csv")
data12 = pd.read_csv("RealFinalData2012.csv")
data13 = pd.read_csv("RealFinalData2013.csv")
data14 = pd.read_csv("RealFinalData2014.csv")
data15 = pd.read_csv("RealFinalData2015.csv")
data17 = pd.read_csv("RealFinalData2017.csv")
data18 = pd.read_csv("RealFinalData2018.csv")

DataList = [data09, data10, data11, data12, data13, data14, data15, data17, data18]
# x1 = [i for i in range(data09["SJV"].shape[0])]
# x2 = [i for i in range(data18["SJV"].shape[0])]
# y1 = np.sort(data09["SJV"])
# y2 = np.sort(data18["SJV"])
n = 0


#INIT
g = data09["SJV"].value_counts()
p = figure(title="SJV from Centrum", x_axis_label='KWH/jaar', y_axis_label='Percentage Aansluitingen Laag-Tarief')
yy = []

# X AND Y
x = data09["SJV"]
for i in data09["Soort aan"]:
    if i[0] == "O":
        temp = 0
    else:
        temp = int(i[0]) * int(i[2:])
    yy.append(temp)
y = np.array(yy)
y = y * data09["Aantal Aansluitingen"]
regression = np.polyfit(x, y, 1)
r_x, r_y = zip(*((i, i*regression[0] + regression[1]) for i in range(len(data09["latitude"]))))

#LEKKER PLOTTEN
p.scatter(x, y, line_color=bokeh.palettes.RdYlGn[9][1], alpha= 0.5)
p.line(r_x, r_y, line_width= 4)

output_file("SJV_BELASTINGMAX.html")

show(p)






# with open('RealFinalData2009.csv', 'r') as Data2009, open('RealFinalData2010.csv', 'r') as Data2010, open('RealFinalData2011.csv', 'r') as Data2011, open('RealFinalData2012.csv', 'r') as Data2012, open('RealFinalData2013.csv', 'r') as Data2013, open('RealFinalData2014.csv', 'r') as Data2014, open('RealFinalData2015.csv', 'r') as Data2015, open('RealFinalData2017.csv', 'r') as Data2017, open('RealFinalData2018.csv', 'r') as Data2018:
#     lst1 = []
#     lst2 = []
#     for row in csv.reader(inp):
#         lst1 += [row]
#     for line in csv.reader(geos):
#         lst2 += [line]
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
    
