import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib
import numpy as np

data = pd.read_csv("FinalData\Data2018.csv")


fig = plt.figure()
ax = fig.add_subplot(111)
bx = fig.add_subplot(111)
x, y, a = [], [], []
t = np.array([])
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
        
xall = [i for i in range(len(a))]
yall = sorted(a)

ax.scatter(x, y, c=t, cmap='magma_r', s=(t/15000)**3, alpha = 0.8, marker='$\odot$', norm=matplotlib.colors.LogNorm())
            # ax.plot(x, y, marker = '.', markersize = '0.3', linestyle='None', color = "red")

bx.scatter(xall, yall)

x0, x1 = 4.812657, 4.988321
y0, y1 = 52.318159, 52.424294        
# x0, x1 = ax.get_xlim()
# y0, y1 = ax.get_ylim()
img = plt.imread("amsterdamhdmap.png")
ax.imshow(img, extent = [x0, x1, y0, y1], aspect = "auto", zorder = 0)

plt.savefig("initialPlots\initialPlot2018.png", dpi = 1300)