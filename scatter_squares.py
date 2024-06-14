import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots()

x_values = [1, 2, 3, 4]
y_values = [2, 4, 9, 16]
ax.scatter(x_values, y_values, s=100)

ax.set_title("Scatter Square Numbers")
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square 0f Value", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()