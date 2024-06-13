import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4]
squares = [1, 4, 9, 16]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置标题和轴标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置刻度样式
ax.tick_params(labelsize=14)
plt.show()
