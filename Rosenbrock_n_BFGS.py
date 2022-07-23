# -------------------------------------------------
# BFGS法求解the extended Rosenbrock function最小值
# -------------------------------------------------
import numpy as np


def rosenbrock_n(x, n):
    """
    the extended Rosenbrock function
    :param x: 自变量x
    :param n: 维度n
    :return:
    """
    ret = 0
    for i in range(n - 1):
        ret += 100 * (x[i + 1] - x[i] ** 2) ** 2 + (1 - x[i]) ** 2
    return ret


def grad(x, n: int):
    """
    the extended Rosenbrock function梯度
    :param x: 自变量x
    :param n: 维度n
    :return:
    """
    if n % 2 != 0:
        return np.array([])
    retgrad = []
    for i in range(n):
        if i == 0:
            retgrad.append(400 * x[i] ** 3 - 400 * x[i] * x[i + 1] + 2 * x[i] - 2)
        elif i == n - 1:
            retgrad.append(-200 * x[i - 1] ** 2 + 200 * x[i])
        else:
            retgrad.append((400 * x[i] ** 3 - 400 * x[i] * x[i + 1] + 2 * x[i] - 2) + (-200 * x[i - 1] ** 2 + 200 * x[i]))
    return np.array(retgrad)


def BFGS(x0, n):
    """
    BFGS求解算法
    :param x0: 初始位置x0
    :param n: 维度n
    :return: 迭代过程记录
    """
    maxk = 10000  # 设置最大次数
    W = np.zeros((n, maxk))  # 结果记录buffer
    W[:, 0] = x0
    x = x0  # 设置起始点
    i = 0  # 记录迭代次数
    df_max = 1e-5  # 停止迭代时梯度阈值
    Bk = np.eye(n)  # 初始化为单位矩阵
    while np.linalg.norm(grad(x, n)) > df_max and i < maxk:
        # 计算前进方向
        p = -np.linalg.solve(Bk, grad(x, n))
        # Armijo求解步长
        rho = 0.55
        sigma = 0.2
        m = 0
        alpha = 0
        while m < 20:
            newf = rosenbrock_n(x + rho ** m * p, n)
            oldf = rosenbrock_n(x, n)
            if newf < oldf + sigma * rho ** m * np.dot(grad(x, n).T, p):
                alpha = rho ** m
                break
            m += 1
        # 计算新的迭代点
        xk_1 = x + alpha * p
        # 更新Bk
        sk = xk_1 - x
        yk = grad(xk_1, n) - grad(x, n)
        Bk = Bk - np.outer(np.dot(Bk, sk), np.dot(sk.T, Bk)) / np.dot(np.dot(sk.T, Bk), sk) + np.outer(yk, yk.T) / np.dot(yk.T, sk)
        # 数据迭代
        x = xk_1
        # 数据记录
        W[:, i + 1] = x  # 记录当前位置
        i += 1  # 计算迭代次数
    print(f'维度：{n}')
    print(f"迭代次数为：{i}")
    print(f"近似解为：{x}")
    print(f"函数值为：{rosenbrock_n(x, n)}")
    print(f"当前位置梯度范数：{np.linalg.norm(grad(x, n))}")
    W = W[:, 0:i + 1]
    return W


if __name__ == '__main__':
    x0 = np.array([-1.2, 1, -1.2, 1, -1.2, 1, -1.2, 1])
    n = x0.size
    W = BFGS(x0, n)
