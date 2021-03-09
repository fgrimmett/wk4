import matplotlib.pyplot as plt
import math
import numpy as np

numpoints = 300
xmin = 0
xmax = 20

x = np.linspace(xmin, xmax, numpoints)
y = np.sin(x)

plt.plot(x, y)
plt.show()