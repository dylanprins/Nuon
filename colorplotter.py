import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib
import numpy as np

data = pd.read_csv("FinalData\Data2017.csv")
data2 = pd.read_csv("Zonneenergie\zon2017.csv")

fig = plt.figure()
ax = fig.add_subplot(111)
bx = fig.add_subplot(111)
x, y, a, xx, yy = [], [], [], [], []
t, g = np.array([]), np.array([])
for i in range(len(data["longitude"])):
    if data["longitude"][i] < 52.424294 and data["longitude"][i] > 52.318159:
        if data["latitude"][i] > 4.812657 and data["latitude"][i] < 4.988321:
            y.append(data["longitude"][i])
            x.append(data["latitude"][i])
            temp = np.array([data["SJV"][i]])
            # sizetemp = np.array((data["SJV"][i]/20000) ** 1.2)
            a.append(data["SJV"][i])
            # size = np.concatenate([t, sizetemp])
            t = np.concatenate([t, temp])

for i in range(len(data2["lon"])):
    if data2["lat"][i] < 52.424294 and data2["lat"][i] > 52.318159:
        if data2["lon"][i] > 4.812657 and data2["lon"][i] < 4.988321:
            yy.append(data2["lat"][i])
            xx.append(data2["lon"][i])
            temp2 = np.array([data2["kwp"][i]])
            g = np.concatenate([g, temp2])
# print(x)      
# xall = [i for i in range(len(a))]
# yall = sorted(a)

# ax.scatter(x, y, c=t, cmap='magma_r', s=(t/15000)**3, alpha = 0.9, marker='$\odot$', norm=matplotlib.colors.LogNorm())
ax.scatter(xx, yy, c=g, cmap='viridis', s=(g/10000)**2)

# bx.scatter(xall, yall)

x0, x1 = 4.812657, 4.988321
y0, y1 = 52.318159, 52.424294        
# x0, x1 = ax.get_xlim()
# y0, y1 = ax.get_ylim()
img = plt.imread("amsterdamhdmap.png")
ax.imshow(img, extent = [x0, x1, y0, y1], aspect = "auto", zorder = 0)
# plt.scatter(xx, yy)
# plt.show()
plt.savefig("initialPlots\initialzonPlot2017.png", dpi = 1300)