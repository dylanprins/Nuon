from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn

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
        if c > 1:
            if c == 6:
                mediaan.append(row[2])
                gemiddelde.append(row[3])
                standaarddeviatie.append(row[4])
            jaar.append(row[0])
            verbruik.append(row[1])

for i in range(9):
    mediaan.append('')
    gemiddelde.append('')
    standaarddeviatie.append('')

print(jaar)
print(verbruik)
print(mediaan)
print(gemiddelde)
print(standaarddeviatie)

output_file("data_table.html")

data = dict(
        jaar=jaar,
        verbruik=verbruik,
        mediaan=mediaan,
        gemiddelde=gemiddelde,
        standaarddeviatie=standaarddeviatie,
    )
source = ColumnDataSource(data)

columns = [
        TableColumn(field="jaar", title="Jaar"),
        TableColumn(field="verbruik", title="Verbruik"),
        TableColumn(field="mediaan", title="Mediaan"),
        TableColumn(field="gemiddelde", title="Gemiddelde"),
        TableColumn(field="standaarddeviatie", title="σ"),
    ]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

show(widgetbox(data_table))