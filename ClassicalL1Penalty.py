# ------------------------------------
# 使用l1精确罚函数进行求解
# ------------------------------------
import numpy as np
from matplotlib import pyplot as plt
import time
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


def QPM(X0: np.ndarray, max_iter=1000):
    """
    二次罚函数求解
    :param X0: 求解初值
    :param max_iter: 最大迭代次数
    :return:
    """
    # 实例化求解目标函数与约束条件
    fun = Function()
    cons = Constraint()
    # 初始化可迭代参数
    xk = X0                         # 迭代位置，初始为x0
    mu_k = 3                        # 惩罚因子
    rate = 1.2                      # 乘法因子更新比例
    iter_index = 0                  # 记录迭代次数
    route_get = [[xk[0]], [xk[1]]]  # 记录迭代路径
    # 判断初值位置所在约束条件，设置激活标志位
    active_flag = ((np.dot(cons.ai, xk) + cons.b) < np.zeros(cons.cons_len)).astype(np.int)
    # 开始迭代
    while iter_index < max_iter:
        # 获取新的目标函数参数
        H = fun.G
        B = fun.c + 0.5 * np.dot(xk.T, fun.G) + 0.5 * np.dot(fun.G.T, xk)
        for i in range(cons.cons_len):
            B = B - active_flag[i] * mu_k * cons.ai[i].T
        # 求解当前状态下的近似解
        pk = -np.dot(np.linalg.inv(H), B)
        # 求解步长因子
        ak = np.array([-(cons.b[i] + np.dot(cons.ai[i].T, xk)) / np.dot(cons.ai[i].T, pk) if active_flag[i] else 1 for i in range(cons.cons_len)], dtype=np.float)
        ak = np.min(ak)
        # 位置迭代，使用步长因子与步长相乘的方式进行迭代会快非常多(xk = xk + ak * pk)，使用常规迭代方法会慢很多(xk = xk + pk)
        # 暂时不知道是不是程序设计错误/理论推导错误导致的原方法计算比较慢
        xk = xk + ak * pk
        # xk = xk + pk
        # 更新约束激活标志位
        active_flag = ((np.dot(cons.ai, xk) + cons.b) < np.ones(cons.cons_len) * (-1e-5)).astype(np.int)
        # 更新惩罚因子
        mu_k = mu_k * rate
        # 记录当前迭代位置
        route_get[0].append(xk[0])
        route_get[1].append(xk[1])
        print(f'iter times:{iter_index}, xk: {xk}, active flag: {active_flag}, mu_k: {mu_k}')
        if np.sum(active_flag) == 0:
            # 如果当前数值满足约束条件，则直接返回
            break
        # 迭代次数加一
        iter_index += 1
    # 输出迭代结果
    print(f'初始位置x0: ({X0[0]}, {X0[1]})')
    print(f'迭代次数为：{iter_index}')
    print(f'迭代结果：(%.4f, %.4f)， 函数值：{fun.fun([xk[0], xk[1]])}' % (xk[0], xk[1]))
    return route_get


if __name__ == '__main__':
    start_time = time.time()
    x0 = np.array([1, 0.5], dtype=np.float)
    route = QPM(x0)
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
