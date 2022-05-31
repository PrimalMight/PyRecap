import numpy as np

z0 = 1j + 1

c = -0.1 + 0.65i
z_max = 10
n_max = 500
z_n = 0

while(z_n <= n_max or abs(z_n) > z_max):  
    z_n = z_n*z_n + c
    

img = np.zeros((500, 500))
