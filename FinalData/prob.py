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
ColorList = ['red', 'green', 'blue', 'purple']
# x1 = [i for i in range(data09["SJV"].shape[0])]
# x2 = [i for i in range(data18["SJV"].shape[0])]
# y1 = np.sort(data09["SJV"])
# y2 = np.sort(data18["SJV"])
n = 0
print(bokeh.palettes.Category20)


g = data09["SJV"].value_counts()
print(g.keys()[0])
p = figure(title="SJV from Centrum", x_axis_label='KWH/jaar', y_axis_label='Percentage Aansluitingen Laag-Tarief')

x = data09["SJV"]
y = (data09["longitude"] - 52.373852) + (data09["latitude"] - 4.898199)
# longitude,latitude
# 52.373852, 4.898199
# for i in DataList:
#     x = [j for j in range(i["SJV"].shape[0])]
#     y = np.sort(i["SJV"])
p.scatter(x, y, line_color=bokeh.palettes.RdYlGn[9][1])
#     n += 1
output_file("SJV_Centrum.html")


# p.line(x1, y1)
# p.line(x2, y2, line_color = "red")

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
    
