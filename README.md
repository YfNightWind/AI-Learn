### 基于规则自动生成的人类语句，自动出数学题

> 复合句子 = 句子｜句子 连词 复合句子
> 句子 = 主语s 谓语 宾语s
> 主语 = 冠词 定语 名词｜冠词 定语 代词
> 宾语 = 冠词 定语 名词｜冠词 定语 代词
> 主语s = 主语 和 主语｜主语
> 宾语s = 宾语 和 宾语｜宾语
> 代号 = 名词｜代词
> ⬇️
> 主语 = 冠词 定语 代号
> 宾语 = 冠词 定语 代号
---
##### example
> 名词 = 苹果｜西瓜｜小猫｜小明
> 代词 = 你｜我｜他｜他们｜你们｜我们｜它
> 定语 = 漂亮的｜安静的｜可爱的｜今天的｜神秘的
> 冠词 = 一个｜一只｜这个｜那个
> 连词 = 和｜但是｜而且｜不过
> 谓词 = 吃｜看见｜喊｜摘｜摸
---
##### Code
```python
grammer_rule = '''

复合句子 = 句子 | 句子 连词 复合句子
句子 = 主语s 谓语 宾语s
主语 = 冠词 定语 名词 | 冠词 定语 代词
宾语 = 冠词 定语 名词 | 冠词 定语 代词
主语s = 主语 和 主语 | 主语
宾语s = 宾语 和 宾语 | 宾语
代号 = 名词 | 代词
主语 = 冠词 定语 代号
宾语 = 冠词 定语 代号
名词 = 苹果 | 西瓜 | 小猫 | 小明
代词 = 你 | 我 | 他 | 他们 | 你们 | 我们 | 它
定语 = 漂亮的 | 安静的｜可爱的 | 今天的 | 神秘的
冠词 = 一个 | 一只 | 这个 | 那个
连词 = 和 | 但是 | 而且 | 不过
谓词 = 吃 | 看见 | 喊 | 摘 | 摸
'''
grammer_rule = '''

复合句子 = 句子｜句子 连词 复合句子
句子 = 主语s 谓语 宾语s
主语 = 冠词 定语 名词｜冠词 定语 代词
宾语 = 冠词 定语 名词｜冠词 定语 代词
主语s = 主语 和 主语｜主语
宾语s = 宾语 和 宾语｜宾语
代号 = 名词｜代词
主语 = 冠词 定语 代号
宾语 = 冠词 定语 代号
名词 = 苹果｜西瓜｜小猫｜小明
代词 = 你｜我｜他｜他们｜你们｜我们｜它
定语 = 漂亮的｜安静的｜可爱的｜今天的｜神秘的
冠词 = 一个｜一只｜这个｜那个
连词 = 和｜但是｜而且｜不过
谓词 = 吃｜看见｜喊｜摘｜摸
'''


def parse_grammer(rule):
    # 定义一个字典
    grammer = dict()

    for line in grammer_rule.split('\n'):
        # 去掉空行
        if not line.split():
            continue
        # print(line)
        # 等于号左边相当于目标，右边的是扩展，能不能实现给出的目标，返回后面扩展
        # target = 等号左边，expand = 等号右边
        target, expand = line.split('=')
        expands = expand.split('｜')
        # print(target)
        # print(expands)
        # 去掉空格
        grammer[target.strip()] = [e.strip() for e in expands]
    return grammer

```
测试案例
```python
def get_expands(target, grammer):
    return grammer[target]


if __name__ == '__main__':
    print(get_expands('复合句子', parse_grammer(grammer_rule)))
```
```python
# expands再扩展，扩展到不能在扩展为止
def gene(target, grammer):
    if target not in grammer:
        return target
    expand = random.choice(grammer[target])
    return ''.join([gene(e, grammer) for e in expand.split()])


if __name__ == '__main__':
    for i in range(10):
        print(gene('句子', parse_grammer(grammer_rule)))
```
结果可能如下：
```
一个今天的苹果谓语一只可爱的你和那个神秘的你们
一个今天的他们谓语那个安静的他和一只漂亮的我们
一个可爱的小明和这个神秘的他们谓语一只安静的你和一个今天的苹果
这个神秘的小猫谓语一个漂亮的他们
一个今天的你们谓语一个神秘的它
那个神秘的小猫和一个安静的你们谓语一个漂亮的我们
那个安静的我们谓语这个神秘的我
一个漂亮的小猫和这个漂亮的他谓语这个今天的我们
一个今天的西瓜和那个漂亮的他谓语一只漂亮的苹果
一只漂亮的小猫谓语那个可爱的小明
```
---
### 倒水问题
> 初始有一个90ml的杯子和40ml的杯子，杯子是没有刻度的
> 要先定义操作，P为水池
> A->P A往水池倒水
> P->A 水池P装入A
> B->P
> P->B
> A->B
> B->A
> 初始状态为(x, y) ➡️ 期望为(60, -)或(-, 60)
> 从(90, 40)开始，会出现非常多种情况，形成一种类似散装图（树）只要其中有一个符合期望就可以
```python
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


print(success(10, 20, 90, 40))
print(success(0, 0, 90, 40))  # 字典有个方面，键相同时会覆盖，只输出相同的键最后一个值
```
*Output*
``` 
{(0, 20): '倒空x', (10, 20): '倒空y', (0, 30): 'x倒入y', (30, 0): 'y倒入x', (90, 0): '装满x', (10, 40): '装满y'}
{(0, 0): 'y倒入x', (90, 0): '装满x', (0, 40): '装满y'}
```
```python
goal = 60
capacity1, capacity2 = 90, 40  # 定义最大容量
# 假设路径初始状态，路径用列表的形式表示
paths = [[("init", (0, 0))]]
# 现在不需要看这个paths，不断搜索这条路的边沿，再沿每条路继续往下扩展
while paths:
    # 当发现还有路径可搜索时，这里取任意路径
    path = paths.pop(0)
    # 取路径当边沿，path的最右边
    frontier = path[-1]
    # (x, y)就是边沿状态
    (x, y) = frontier[-1]

    # item(), 取键给state，值给action
    for state, action in success(x, y, capacity1, capacity2).items():
        # 一开始设定了初始值(0,0)，以及两个杯子容量设置的都是满的
        print(frontier, state, action)
```
*Output*
```
('init', (0, 0)) (0, 0) y倒入x
('init', (0, 0)) (90, 0) 装满x
('init', (0, 0)) (0, 40) 装满y
```
```python
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


```
*Output*
```
==>
('init', (0, 0))
==>
('装满y', (0, 40))
==>
('y倒入x', (40, 0))
==>
('装满y', (40, 40))
==>
('y倒入x', (80, 0))
==>
('装满y', (80, 40))
==>
('y倒入x', (90, 30))
==>
('倒空x', (0, 30))
==>
('y倒入x', (30, 0))
==>
('装满y', (30, 40))
==>
('y倒入x', (70, 0))
==>
('装满y', (70, 40))
==>
('y倒入x', (90, 20))
==>
('倒空x', (0, 20))
==>
('y倒入x', (20, 0))
==>
('装满y', (20, 40))
==>
('y倒入x', (60, 0))
```
