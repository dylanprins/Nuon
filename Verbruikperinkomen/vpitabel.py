from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.io import output_file, show, vform

import csv
c=0
jaar = []
verbruik = []
mediaan=[]
gemiddelde=[]
standaarddeviatie=[]

with open('../Verbruikperinkomen/nongraphic.csv', 'r') as inp:
    data = csv.reader(inp)
    for row in data:
        c+=1
        jaar.append(row[0])
        verbruik.append(row[1])
        if c == 6:
            mediaan.append(row[2])
            gemiddelde.append(row[3])
            standaarddeviatie.append(row[4])




output_file("data_table.html")

data = dict(
        dates=[],
        downloads=[],
    )
source = ColumnDataSource(data)

columns = [
        TableColumn(field="dates", title="Date", formatter=DateFormatter()),
        TableColumn(field="downloads", title="Downloads"),
    ]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

show(vform(data_table))