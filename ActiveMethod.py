# ------------------------------------
# 活跃集方法求解源码
# ------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import time
import psutil
import os


class Function:
    def __init__(self):
        self.G = np.array([
            [2, -2],
            [-2, 4]
        ])
        self.c = np.array(
            [
                -2,
                -6
            ]
        )

    def fun_numpy(self, x: np.ndarray) -> np.ndarray:
        return 0.5 * np.dot(np.dot(x.T, self.G), x) + np.dot(x.T, self.c)

    def fun(self, x):
        x1, x2 = x
        return x1 ** 2 + 2 * x2 ** 2 - 2 * x1 - 6 * x2 - 2 * x1 * x2


class Workspace:
    def __init__(self):
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

    def getValue(self, x: np.ndarray) -> np.ndarray:
        return np.dot(self.ai, x) + self.b


def getAlpha(W, xk, pk):
    """
    根据工作集计算出所有的步长
    :param W: 当前的工作集（活跃集）
    :param xk:
    :param pk: 计算得到步长
    :return:
    """
    b = Workspace().b
    ai = Workspace().ai
    res = []
    min_index = 0
    for i in range(len(W)):
        if not W[i]:
            ak = -(b[i] + np.dot(ai[i].T, xk)) / np.dot(ai[i].T, pk)
            if np.dot(ai[i].T, pk) < 0:
                # 如果满足条件，则记录当前ak
                res.append(ak)
                # 记录最小ak对应下标
                if ak <= res[min_index]:
                    min_index = i
            else:
                res.append(1)
        else:
            res.append(1)
    return np.array(res), min_index


def ActiveSetMethod(x0, max_iter):
    """
    积极集求解方法
    :param x0: 初值
    :param max_iter: 迭代最大次数
    :return:
    """
    # 实例化函数与工作集
    fun = Function()
    workspace = Workspace()
    # 判断初值所在工作集
    W_value = workspace.getValue(x0)
    W = np.zeros(len(W_value), dtype=np.int)  # 0 -> 表示当前工作集无效，1 -> 表示当前工作集有效
    for i in range(len(W_value)):
        if W_value[i] == 0:
            W[i] = True
    print(f'init workspace:{W}')
    # 固定参数设置
    G = fun.G
    c = fun.c
    ai = Workspace().ai
    # 迭代参数设置
    xk = x0
    gk = np.dot(G, xk) + c
    iter_times = 0  # 记录迭代次数
    route_get = [[xk[0]], [xk[1]]]  # 记录迭代路径
    ak = 1
    # 开始积极集迭代
    while iter_times < max_iter:
        # 拉格朗日乘子法求解等式约束子问题步长
        p0, p1 = symbols('p0,p1')
        l0, l1, l2, l3 = symbols('l0,l1,l2,l3')
        f = p0 ** 2 + 2 * p1 ** 2 - 2 * p0 * p1 + gk[0] * p0 + gk[1] * p1               # 目标函数
        g0 = W[0] * (ai[0][0] * p0 + ai[0][1] * p1)
        g1 = W[1] * (ai[1][0] * p0 + ai[1][1] * p1)
        g2 = W[2] * (ai[2][0] * p0 + ai[2][1] * p1)
        g3 = W[3] * (ai[3][0] * p0 + ai[3][1] * p1)
        target = f - l0 * g0 - l1 * g1 - l2 * g2 - l3 * g3
        target_diff = [
            diff(target, p0),
            diff(target, p1),
            diff(target, l0),
            diff(target, l1),
            diff(target, l2),
            diff(target, l3)
        ]
        var_list = [p0, p1, l0, l1, l2, l3]
        res = solve(target_diff, var_list)
        pk = np.array([res[p0], res[p1]])
        # TODO：当步长为0时，判断lambda>=0是否对所有活跃集都成立
        if pk[0] == 0 and pk[1] == 0:
            flag = True
            min_index = 0
            # 遍历所有工作集，判断KKT条件是否成立，以及找到最小值下标
            for i in range(len(W)):
                if W[i]:
                    # 找到最小的lambda对应的下标
                    if min_index == 0:
                        min_index = i
                    else:
                        if res[var_list[i + 2]] < res[var_list[min_index + 2]]:
                            min_index = i
                    # 判断是否所有的lambda都大于等于0
                    if res[var_list[i + 2]] < 0:
                        flag = False
            # 如果KKT条件成立，则说明当前为最小值，否则将最小值下标添加进工作集
            if flag:
                break
            else:
                W[min_index] = False
        # TODO：当步长不为0时，计算ak，并进行迭代
        else:
            ak_list, min_index = getAlpha(W, xk, pk)  # 根据所有非活跃集，求解得到所有ak，取值范围为(0, 1]
            ak = min(1, np.min(ak_list))  # 获取最小的值作为ak
            if ak < 1:
                # 如果ak小于1，即说明存在block constrain，将对应的block constrain加入工作集
                W[min_index] = True
            xk = xk + ak * pk
            gk = np.dot(G, xk) + c
        # 记录当前迭代位置
        route_get[0].append(xk[0])
        route_get[1].append(xk[1])
        # 迭代次数累加
        iter_times += 1
        print(f'{iter_times}--ak:{ak}--pk:{pk}--xk:{xk}--workspace:{W}--Lagrange result:{res}')
    print(f'初始位置x0: ({x0[0]}, {x0[1]})')
    print(f'迭代次数：{iter_times}')
    print(f'迭代结果：({xk[0]}, {xk[1]})， 函数值：{fun.fun([xk[0], xk[1]])}')
    return route_get


if __name__ == '__main__':
    start_time = time.time()
    x0 = np.array([1/4, 1/3], dtype=np.float)
    route = ActiveSetMethod(x0, 10)
    print('Memory consumption：%.2f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
    print(f'程序运行时间: {time.time() - start_time}s')

    X1 = np.arange(-0.5, 2.5, 0.05)
    X2 = np.arange(-0.5, 1.5, 0.05)
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
