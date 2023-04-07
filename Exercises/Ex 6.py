import numpy as np

ex5 = np.array([[10, 50, 70, 20, 40], [5, 45, 95, 35, 65]])
np.savetxt("ex6.txt", ex5, fmt="%d")
loaded_array = np.loadtxt("ex6.txt")
print(loaded_array)
