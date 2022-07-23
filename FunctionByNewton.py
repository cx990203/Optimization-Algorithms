import numpy as np
import random
from copy import deepcopy


# Beale函数
def function(x):
    return 0.5 * ((x[1] - x[0] ** 2) ** 2 + (1 - x[1]) ** 2)


# 梯度方向
def grad(x):
    return np.array([
        (-2) * (x[0] * x[1] - x[0] ** 3),
        (x[1] - x[0] ** 2) - (1 - x[1])
    ], dtype=np.float)


# Hessian矩阵
def hess(x):
    return np.array([
        [
            (-2) * (x[1] - 3 * x[0] ** 2),
            (-2) * x[0]
        ],
        [
            (-2) * x[0],
            2
        ]
    ], dtype=np.float)


# 牛顿法迭代过程
def newton(x0):
    x_start = deepcopy(x0)
    maxk = 10000  # 设置最大次数
    W = np.zeros((2, maxk + 1))  # 结果记录buffer
    W[:, 0] = x0
    x = x0  # 设置起始点
    i = 0  # 记录迭代次数
    df_max = 1e-5  # 停止迭代时梯度阈值
    while np.linalg.norm(grad(x)) > df_max and i < maxk:
        H = hess(x)     # 求解hession矩阵
        p = -np.dot(np.linalg.inv(H), grad(x))  # 计算前进方向
        x += p  # 计算新的迭代点
        W[:, i + 1] = x     # 记录当前位置
        i += 1      # 计算迭代次数
    print(f"起始点为：{x_start}")
    print(f"迭代次数为：{i}")
    print(f"近似解为：{x}")
    print(f"函数值为：{function(x)}")
    print(f"当前位置梯度范数：{np.linalg.norm(grad(x))}")
    W = W[:, 0:i]
    return W, 'x0=%.2f,x1=%.2f\\%d\\x0=%.2f,x1=%.2f)' % (x_start[0], x_start[1], i, x[0], x[1])


if __name__ == "__main__":
    times = 20
    res = []
    for i in range(times):
        x0 = np.array([10 * (random.random() - random.random()), 10 * (random.random() - random.random())], dtype=np.float)
        W, res_str = newton(x0)
        res.append(res_str)
    with open('res.txt', 'w') as f:
        for obj in res:
            print(obj)
            f.write(obj + '\n')

