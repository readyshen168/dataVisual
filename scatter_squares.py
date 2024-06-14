import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots()

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
ax.scatter(x_values, y_values, s=0.6)

ax.set_title("Scatter Square Numbers")
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square 0f Value", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()