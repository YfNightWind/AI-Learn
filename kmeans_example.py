"""
kmeans 里最方要的是找中心点

1.明确输入、输出分別是什么，怎么用数学来表达
2.初始化：类別数K=？、类中心
3.所有的点points0都和当前选中的中心点分别计算一次距离，然后判断高哪个中心点距离最近，就归到哪一类
K1: {pi, pj, ....pm} Ω1 means1= ((xi+xj+))
K2: {pa, pb,....}     Ω2
K3: {px, py,....}       Ω3
4. 更新中心点
通过求平均值更新中心点
Ω1 means1= ( (xi + yj +... xm)/m, (yi + yj +.... ym）/m）)
Ω2
Ω3
5.当前的中心点和前一次中心点非常接近
这时候就是我们要得到的中心点，停止送代了
"""
import random

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BASE_COLORS
from collections import defaultdict

# 输入数据
points0 = np.random.normal(size=(100, 2))
# 初始化
K = 3
points1 = np.random.normal(loc=1, size=(100, 2))
points2 = np.random.normal(loc=2, size=(100, 2))
points3 = np.random.normal(loc=5, size=(100, 2))


# 随机初始化中心点(要在points范围里面)
# 随机产生k=3组中心点，就是初始化数据的x, y李分别随机选出一组(x, y)
def random_centers(k, points):
    for i in range(k):
        yield random.choice(points[:, 0]), random.choice(points[:, 1])


def distance(p1, p2):
    x1, x2 = p1
    y1, y2 = p2
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def mean(points):
    all_x, all_y = [x for x, y in points], [y for x, y in points]
    x_m = np.mean(all_x)  # 求均值
    y_m = np.mean(all_y)
    # 返回中心点坐标
    return x_m, y_m


# 实现
def kmeans(k, points, centers=None):
    colors = list(BASE_COLORS.values())
    if not centers:
        centers = list(random_centers(k, points))

    print(centers)
    # print(points)
    # 分别把三个中心点画出来
    for i, c in enumerate(centers):
        plt.scatter([c[0]], [c[1]], s=90, marker='*', c=colors[i])
    # 画出原始输入数据
    plt.scatter(*zip(*points), c='black')
    # 离中心点最近的点
    centers_neighbor = defaultdict(set)
    # 原始输入points的点和中心点计算距离、分组
    for p in points:
        # 求最小值，离每个center的距离最小的点，返回给closest_c
        closest_c = min(centers, key=lambda c: distance(p, c))
        # 把每一组用字典表达出来，key是closet_c
        centers_neighbor[closest_c].add(tuple(p))

    # 把每一组点用不同颜色画出来
    for i, c in enumerate(centers):
        _points = centers_neighbor[c]
        all_x, all_y = [x for x, y in _points], [y for x, y in _points]
        plt.scatter(all_x, all_y, c=colors[i])

    plt.show()

    # 更新中心点
    new_center = []
    for c in centers_neighbor:
        new_c = mean(centers_neighbor[c])
        new_center.append(new_c)
    # 判断前后两次中心点的距离，如果小于阈值就停止，否则继续迭代
    distances_old_and_new = [distance(c_old, c_new) for c_old, c_new in zip(centers, new_center)]
    print(distances_old_and_new)

    threshold = 0.4  # 设置阈值
    if all(c < threshold for c in distances_old_and_new):
        return centers_neighbor
    else:
        kmeans(K, points, new_center)


kmeans(3, points0)
