import matplotlib.pyplot as plt

sizes = [15, 30, 25, 10, 20]
labels = ['Rosu', 'Albastru', 'Verde', 'Mov', 'Portocaliu']
colors = ['red', 'blue', 'green', 'purple', 'orange']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, shadow=True)
ax.set_title('Pie Chart with Custom Colors and Shadow')
plt.show()
