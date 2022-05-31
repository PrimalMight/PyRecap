import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 10)
x2 = np.linspace(-2, 0, 10)
y2 = np.cos(x/(x*x-3))
y = np.pi * np.sin(x*x) + np.exp(-(x*x))


plt.plot(x,y)
plt.plot(x2,y2)
plt.show(block=True)