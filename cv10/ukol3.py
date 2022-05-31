import matplotlib.pyplot as plt
import numpy as np

img = np.zeros((100, 100))

a = 25
b = 25

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r = i + j
        if i < a and j < b:
            img[i, j] = r


plt.imshow(img)
plt.show
plt.show(block=True)