import matplotlib.pyplot as plt
from random_walk import RandomWalk

plt.style.use('dark_background')
# 调整Matplotlib的输出尺寸
fig, ax = plt.subplots(figsize=(16,9))

# 新建随机游走类
rw = RandomWalk()

point_numbers = range(rw.num_points)

ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
# 标红第一个点
ax.scatter(rw.x_values[0], rw.y_values[0], c='red', edgecolors='none', s=50)
# 标绿最后一个点
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none', s=50)

# 隐藏坐标轴
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)

# 打印最后一个点
print(f"x:{rw.x_values[-1]}, y:{rw.y_values[-1]}")

# 让两条坐标轴上的刻度间距相等
ax.set_aspect('equal')
plt.show()
