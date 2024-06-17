import matplotlib.pyplot as plt
from random_walk import RandomWalk

plt.style.use('dark_background')
fig, ax = plt.subplots()

# 新建随机游走类
rw = RandomWalk()

point_numbers = range(rw.num_points)

ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
# 标红第一个点
ax.scatter(rw.y_values[0], rw.x_values[0], c='red', edgecolors='none', s=50)
# 标绿最后一个点
ax.scatter(rw.y_values[-1], rw.x_values[-1], c='green', edgecolors='none', s=50)

# 让两条坐标轴上的刻度间距相等
ax.set_aspect('equal')
plt.show()
