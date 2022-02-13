import random

'''梯度下降法
loss=((wx+b)-y)**2
'''


def loss(x, w, b, y):
    return ((w * x + b) - y) ** 2


# 求偏导
def gradient(w, x, b, y):
    return 2 * (w * x + b - y) * x


w, b = random.randint(-10, 10), random.randint(-10, 10)

x, y = 0.2, 0.35

print(loss(x, w, b, y))

# 迭代
for i in range(10):
    w_gradient = gradient(w, x, b, y)
    w = w - w_gradient
    print("w = ", w)
    print()
    print("loss = ", loss(x, w, b, y))
