from random import choice


class RandomWalk:
    """一个生成随机游走数据的类"""

    def __init__(self, num_points=10000):
        """初始化随机游走的属性"""
        self.num_points = num_points
        # 随机游走的点坐标，从原点开始
        self.x_values = [0]
        self.y_values = [0]

        # 得出随机游走的所有点坐标
        self.fill_walk()

    def fill_walk(self):
        """计算随机游走包含的所有点"""

        # 不断游走，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:

            # 随机决定前进的方向以及距离
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4,5])
            x_step = x_distance * x_direction

            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4,5])
            y_step = y_distance * y_direction

            # 禁止原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 加入新的游走坐标
            self.x_values.append(self.x_values[-1]+x_step)
            self.y_values.append(self.y_values[-1]+y_step)


