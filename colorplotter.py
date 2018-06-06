import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

data = pd.read_csv("FinalData\Data2018.csv")


fig = plt.figure()
ax = fig.add_subplot(111)
x, y, = [], []
t = np.array([])
for i in range(16549):
    if data["longitude"][i] < 52.424294 and data["longitude"][i] > 52.318159:
        if data["latitude"][i] > 4.812657 and data["latitude"][i] < 4.988321:
            y.append(data["longitude"][i])
            x.append(data["latitude"][i])
            temp = np.array([data["SJV"][i]])
            t = np.concatenate([t, temp])
            
print(t)
ax.scatter(x, y, c=t, cmap='gist_stern', s= 0.3)
            # ax.plot(x, y, marker = '.', markersize = '0.3', linestyle='None', color = "red")
        
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
img = plt.imread("amsterdamhdmap.png")
ax.imshow(img, extent = [x0, x1, y0, y1], aspect = "auto", zorder = 0)
plt.savefig("testplot1.png", dpi = 900)