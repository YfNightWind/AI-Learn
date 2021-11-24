import random

# 句子
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

# 数学
another_rule = '''
expression = (math) op (expression) | math
math = num op num
num = sing_num num | sing_num
sing_num = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
op = + | - | * | / | ^ 
'''


def parse_grammer(rule):
    # 定义一个字典
    grammer = dict()
    for line in rule.split('\n'):
        # 去掉空行
        if not line.split():
            continue
        # print(line)
        # 等于号左边相当于目标，右边的是扩展，能不能实现给出的目标，返回后面扩展
        # target = 等号左边，expand = 等号右边
        target, expand = line.split('=')
        expands = expand.split('|')
        # print(target)
        # print(expands)
        # 去掉空格
        grammer[target.strip()] = [e.strip() for e in expands]
    return grammer


# def get_expands(target, grammer):
#     return grammer[target]
#
#
# if __name__ == '__main__':
#     print(get_expands('复合句子', parse_grammer(grammer_rule)))

# expands再扩展，扩展到不能在扩展为止
def gene(target, grammer):
    if target not in grammer:
        return target
    expand = random.choice(grammer[target])
    # return中间没空格是因为中文之间不需要空格
    return ''.join([gene(e, grammer) for e in expand.split()])


if __name__ == '__main__':
    for i in range(10):
        print(gene('math', parse_grammer(another_rule)))
