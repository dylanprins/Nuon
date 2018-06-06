import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

data = pd.read_csv("FinalData\Data2009.csv")


fig = plt.figure()
ax = fig.add_subplot(111)
a = []
for i in range(len(data["longitude"])):
    if data["longitude"][i] < 52.424294 and data["longitude"][i] > 52.318159:
        if data["latitude"][i] > 4.812657 and data["latitude"][i] < 4.988321:
            # y.append(data["longitude"][i])
            # x.append(data["latitude"][i])
            # temp = np.array([data["SJV"][i]])
            # sizetemp = np.array((data["SJV"][i]/20000) ** 1.2)
            a.append(data["SJV"][i])
            # size = np.concatenate([t, sizetemp])
            # t = np.concatenate([t, temp])
        
yall = [i for i in range(len(a))]
xall = sorted(a)

# ax.scatter(x, y, c=t, cmap='gist_stern', s=(t/15000)**3, alpha = 0.8, marker=r'$\odot$')
#             # ax.plot(x, y, marker = '.', markersize = '0.3', linestyle='None', color = "red")

ax.scatter(xall, yall)
     
# x0, x1 = ax.get_xlim()
# y0, y1 = ax.get_ylim()

plt.savefig("initialPlots\schalen2009.png", dpi = 300)