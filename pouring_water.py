# 初始状态，假设杯子都没水(0, 0)
# 期望状态(60, -), (-, 60)
# 这里需要知道每一步后续操作是什么
# 先定义一个函数来表示状态以及对应的操作

# (x, y)表示当前状态， max_x, max_y表示容器最大容量
def success(x, y, max_x, max_y):
    # 定义一个字典来存储状态
    return {
        (0, y): "倒空x",
        (x, y): "倒空y",
        (x + y - max_y, max_y) if x + y >= max_y else (0, x + y): "x倒入y",
        (max_x, x + y - max_x) if x + y >= max_x else (x + y, 0): "y倒入x",
        (max_x, 0): "装满x",
        (x, max_y): "装满y"
    }


if __name__ == '__main__':
    print(success(10, 20, 90, 40))
    print(success(0, 0, 90, 40))
