import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

y = [2, 4, 8, 9]
dlugosc = len(y)
x = []
for i in range(1, dlugosc + 1):
    x.append(i)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(x, y)  # Plot some data on the axes.
plt.show()
