# 初始状态，假设杯子都没水(0, 0)
# 期望状态(60, -), (-, 60)
# 这里需要知道每一步后续操作是什么
# 先定义一个函数来表示状态以及对应的操作

# (x, y)表示当前状态， max_x, max_y表示容器最大容量
import icecream


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


# print(success(10, 20, 90, 40))
# # {(0, 20): '倒空x', (10, 20): '倒空y', (0, 30): 'x倒入y', (30, 0): 'y倒入x', (90, 0): '装满x', (10, 40): '装满y'}
# print(success(0, 0, 90, 40))  # 字典有个方面，键相同时会覆盖，只输出相同的键最后一个值
# # {(0, 0): 'y倒入x', (90, 0): '装满x', (0, 40): '装满y'}

# 现在不需要看这个paths，不断搜索这条路的边沿，再沿每条路继续往下扩展
# search_solution()用来搜索路径的
def search_solution(capacity1, capacity2, goal, start=(0, 0)):
    # 假设路径初始状态，路径用列表的形式表示
    # 数组里面的元组，元素为(action, state)，不用字典表示了，元组作为每一个搜索的节点
    paths = [[("init", (0, 0))]]
    # 为了避免死循环，设置的变量
    is_explored = set()
    while paths:
        # 当发现还有路径可搜索时，这里取任意路径 pop(0)读取的是"[("init", (0, 0))]"
        path = paths.pop(0)
        # 取路径当边沿，path的最右边
        frontier = path[-1]
        # (x, y)就是边沿状态
        (x, y) = frontier[-1]

        # item(), 取键给state，值给action
        for state, action in success(x, y, capacity1, capacity2).items():
            # print(frontier, state, action)
            # 如果这个状态已经存在，就跳过，继续下一个，避免死循环
            if state in is_explored:
                continue
            # 假设状态尚不存在，把此时此刻的状态添加到路径中
            # 第一个是操作，第二个是状态，根据一开始paths的初始化格式来，而非原先的
            new_path = path + [(action, state)]  # [[(path), (new_path), (new_path)]]

            if goal in state:
                return new_path
            else:
                paths.append(new_path)
                # 只保存状态，因为只要判断状态即可，不需要判断操作
                is_explored.add(state)

    return None


if __name__ == '__main__':
    path = search_solution(90, 40, 60, (0, 0))
    for p in path:
        print("==>")
        print(p)
