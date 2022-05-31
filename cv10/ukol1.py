import numpy as np
x = np.linspace(0, 1, 10)
y = x**2 + x
z = y * x
w = np.pi * y[x > 0.3]
z = y[list(range(len(w)))]
z = np.sin(z)
z = w.T