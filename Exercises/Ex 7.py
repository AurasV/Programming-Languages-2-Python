import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.cos(x)

fig, axs = plt.subplots(3, 2, figsize=(10, 10))

axs[0, 0].plot(x, y, 'o', color='purple', markersize=5)
axs[0, 0].set_title('Custom Marker Color')

axs[0, 1].plot(x, y, linestyle='--', linewidth=2)
axs[0, 1].grid(color='gray', linestyle='--', linewidth=0.5)
axs[0, 1].set_title('Custom Line Style and Grid')

axs[1, 0].bar(x, y, color='orange', width=0.2)
axs[1, 0].set_title('Custom Bar Color and Width')

np.random.seed(123)
colors = np.random.rand(len(x))
axs[1, 1].scatter(x, y, c=colors, cmap='viridis')
axs[1, 1].set_title('Scattered Points with Different Colors')

axs[2, 0].plot(x, y, linestyle='-.', color='red', linewidth=1.5)
axs[2, 0].plot(x, -y, linestyle=':', color='blue', linewidth=2.5)
axs[2, 0].set_title('Custom Line Style and Width')

axs[2, 1].barh(x, y, color='green', height=0.2)
axs[2, 1].set_title('Custom Bar Color and Height')

plt.show()
