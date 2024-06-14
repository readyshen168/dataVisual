import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

ax.set_title("Scatter Square Numbers")
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square 0f Value", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()