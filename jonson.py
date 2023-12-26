import json
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

plik = open('temperatury.json', encoding='utf-8')
obj = json.load(plik)

dlugosc = len(obj)
y = []
y2 = []
y3=[]
x = []
x1=[]
b = 0
for i in obj.keys():
    a = obj[i]['temperatura']
    y.append(float(a))
    b += 1
    a2 = obj[i]['wilgotnosc']
    y2.append(float(a2))
    a3=obj[i]['cisnienie']
    y3.append(float(a3))
    x.append(str(b) + "." + str(obj[i]['data'][0:10]) + "\n" +str(obj[i]['data'][11:19]))
    x1.append(str(b))

fig, ax = plt.subplots(3, 1, figsize=(18, 6))  # Create a figure containing a single axes.
ax[0].plot(x1, y, color='red')  # Plot some data on the axes.
ax[1].plot(x1, y2, color='green')
ax[2].plot(x, y3)
ax[0].set_ylabel('*C')
ax[1].set_ylabel('%')
ax[2].set_ylabel('hPa')
plt.show()
plik.close()
