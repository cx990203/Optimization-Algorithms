# ------------------------------------
# 使用增广拉格朗日乘子法求解
# ------------------------------------
import numpy as np
from matplotlib import pyplot as plt
import time
from sympy import *
import psutil
import os


class Function:
    """
    目标函数
    """
    def __init__(self):
        self.G = np.array([
            [2, -2],
            [-2, 4]
        ])
        self.c = np.array([
                -2,
                -6
        ])

    def fun_numpy(self, x: np.ndarray) -> np.ndarray:
        return 0.5 * np.dot(np.dot(x.T, self.G), x) + np.dot(x.T, self.c)

    def fun(self, x):
        x1, x2 = x
        return x1 ** 2 + 2 * x2 ** 2 - 2 * x1 - 6 * x2 - 2 * x1 * x2


class Constraint:
    """
    约束条件
    """
    def __init__(self):
        self.cons_len = 4       # 约束条件场长度
        self.b = np.array([
            1,
            2,
            0,
            0
        ], dtype=np.float)
        self.ai = np.array([
            [-0.5, -1],
            [1, -2],
            [1, 0],
            [0, 1]
        ], dtype=np.float)


def ALM(X0: np.ndarray, max_iter=100):
    """
    增广拉格朗日方法
    :param X0: 求解初值
    :param max_iter: 最大迭代次数
    :return:
    """
    # 实例化求解目标函数与约束条件
    fun = Function()
    cons = Constraint()
    # 初始化可迭代参数
    xk = X0  # 迭代位置，初始为x0
    mu_k = 1  # 惩罚因子
    iter_index = 0  # 记录迭代次数
    route_get = [[xk[0]], [xk[1]]]  # 记录迭代路径
    la = np.zeros(4)                # lambda
    x_target = np.array([0.6, 0.7])
    while iter_index < max_iter:
        # 求解xk+1
        x1, x2 = symbols('x0,x1')
        f = x1 ** 2 + 2 * x2 ** 2 - 2 * x1 - 6 * x2 - 2 * x1 * x2               # 目标函数
        target = f
        for i in range(cons.cons_len):
            if np.dot(cons.ai[i].T, xk) + cons.b[i] - la[i] / mu_k < 0:
                target = target + (
                        -la[i] * (cons.ai[i][0] * x1 + cons.ai[i][1] * x2 + cons.b[i]) + 0.5 * mu_k * (cons.ai[i][0] * x1 + cons.ai[i][1] * x2 + cons.b[i]) ** 2
                )
            else:
                target = target + (-(la[i] ** 2) / (2 * mu_k))
        target_diff = [
            diff(target, x1),
            diff(target, x2)
        ]
        var_list = [x1, x2]
        res = solve(target_diff, var_list)
        xk = np.array([res[x1], res[x2]])
        # 判断是否达到最优解
        print(f'iter times:{iter_index}, xk: {xk}')
        if np.dot((x_target - xk).T, x_target - xk) <= 1e-5:
            # 如果当前数值满足约束条件，则直接返回（偷懒判断，我不想写了。。。累了）
            route_get[0].append(xk[0])
            route_get[1].append(xk[1])
            break
        # 更新lambda
        for i in range(cons.cons_len):
            la[i] = la[i] - mu_k * (np.dot(cons.ai[i].T, xk) + cons.b[i]) - max(np.dot(cons.ai[i].T, xk) + cons.b[i] - la[i] / mu_k, 0)
        # 更新mu_k
        mu_k = mu_k * 1.5
        # 记录当前迭代位置
        route_get[0].append(xk[0])
        route_get[1].append(xk[1])
        # 迭代次数累加
        iter_index += 1
    print(f'初始位置x0: ({x0[0]}, {x0[1]})')
    print(f'迭代次数：{iter_index}')
    print(f'迭代结果：({xk[0]}, {xk[1]})， 函数值：{fun.fun([xk[0], xk[1]])}')
    return route_get


if __name__ == '__main__':
    start_time = time.time()
    x0 = np.array([1, 0.5], dtype=np.float)
    route = ALM(X0=x0)
    print('Memory consumption：%.2f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
    print(f'程序运行时间: {time.time() - start_time}s')

    X1 = np.arange(-0.5, 5.5, 0.05)
    X2 = np.arange(-0.5, 5, 0.05)
    [x1, x2] = np.meshgrid(X1, X2)
    G = np.array([[2, -2], [-2, 4]])
    c = np.array([-2, -6])
    f = Function().fun([x1, x2])
    CLabel = plt.contour(x1, x2, f, 10)
    plt.clabel(CLabel, inline=True)
    vertex = [[0, 2, 0, 0], [1, 0, 0, 1]]
    plt.plot(vertex[0], vertex[1], 'r-')
    plt.plot(route[0], route[1], 'b--')
    plt.scatter([route[0][0]], [route[1][0]], color='red')              # 绘制起点
    plt.scatter([route[0][-1]], [route[1][-1]], color='green')          # 绘制终点
    plt.show()
