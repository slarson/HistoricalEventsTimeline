import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0,100,.5)
y = 2*x**3

plt.semilogx(x,y)
plt.grid(True,which="minor",ls="-")
plt.show()