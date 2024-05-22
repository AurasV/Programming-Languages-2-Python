import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(np.pi + 1, np.pi - 1, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y1, color='blue', label='sin(x)')
ax.plot(x, y2, color='red', label='cos(x)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Intersecting Lines of Different Colors')
plt.show()
