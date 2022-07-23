# -------------------------------------------------
# BFGS法求解the Rosenbrock Function最小值
# -------------------------------------------------
import numpy as np

# Rosenbrock函数
from matplotlib import pyplot as plt


def rosenbrock(x):
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


# 梯度方向
def grad(x):
    return np.array([400 * x[0] ** 3 - 400 * x[0] * x[1] + 2 * x[0] - 2, -200 * x[0] ** 2 + 200 * x[1]])


# wolfe条件计算alpha
def wolfe(f, df, p, x, alpham, c1, c2):
    """
    根据wolfe条件计算alpha
    :param f: 求解函数
    :param df: 倒数
    :param p: 方向
    :param x: 当前位置
    :param alpham: 默认设定步长
    :param c1: 不等式中的系数
    :param c2: 不等式中的系数
    :return: 求解步长
    """
    flag = 0
    # 采用二分法求解步长，a为前边界，b为后边界
    a = 0
    b = alpham
    alpha = 0  # 计算得到步长
    gk = df(x)  # xk位置梯度
    phi0 = f(x)
    dphi0 = np.dot(gk, p)
    while True:
        if flag:
            break
        phi = f(x + alpha * p)  # 计算f(xk+1)
        gk1 = df(x + alpha * p)  # 更新梯度信息
        dphi = np.dot(gk1, p)  # 计算梯度在下降方向上的映射
        if phi <= phi0 + c1 * alpha * dphi0:
            # 满足第一个不等式
            if dphi >= c2 * dphi0:
                # 满足第二个不等式
                flag = 1
            else:
                a = alpha
                b = b
                alpha = (a + b) / 2
        else:
            a = a
            b = alpha
            alpha = (a + b) / 2
    return alpha


# 牛顿法迭代过程
def bfgs(x0):
    maxk = 10000  # 设置最大次数
    W = np.zeros((2, maxk))  # 结果记录buffer
    W[:, 0] = x0
    x = x0  # 设置起始点
    i = 0  # 记录迭代次数
    df_max = 1e-5  # 停止迭代时梯度阈值
    Bk = np.eye(2)   # 初始化为单位矩阵
    while np.linalg.norm(grad(x)) > df_max and i < maxk:
        # bfgs迭代公式
        # 计算前进方向
        p = -np.linalg.solve(Bk, grad(x))
        # p = -np.dot(Bk, grad(x))
        # wolfe条件计算步长
        # alpha = wolfe(rosenbrock, grad, p, x, 0.1, 0.1, 0.9)
        # Armijo求解步长
        rho = 0.55
        sigma = 0.4
        m = 0
        alpha = 0
        while m < 20:
            newf = rosenbrock(x + rho ** m * p)
            oldf = rosenbrock(x)
            if newf < oldf + sigma * rho ** m * np.dot(grad(x).T, p):
                alpha = rho ** m
                break
            m += 1
        # 计算新的迭代点
        xk_1 = x + alpha * p
        sk = xk_1 - x
        yk = grad(xk_1) - grad(x)
        Bk = Bk - np.outer(np.dot(Bk, sk), np.dot(sk.T, Bk)) / np.dot(np.dot(sk.T, Bk), sk) + np.outer(yk, yk.T) / np.dot(yk.T, sk)
        # 数据迭代
        x = xk_1
        # 数据记录
        W[:, i + 1] = x  # 记录当前位置
        i += 1  # 计算迭代次数
    print(f"迭代次数为：{i}")
    print(f"近似解为：{x}")
    print(f"函数值为：{rosenbrock(x)}")
    print(f"当前位置梯度范数：{np.linalg.norm(grad(x))}")
    W = W[:, 0:i + 1]
    return W


if __name__ == "__main__":
    x0 = np.array([-1.2, 1])
    print(rosenbrock(x0))
    print(grad(x0))
    W = bfgs(x0)

    X1 = np.arange(-1.5, 3.2, 0.05)
    X2 = np.arange(-0, 2, 0.05)
    [x1, x2] = np.meshgrid(X1, X2)
    f = 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2
    plt.contour(x1, x2, f, 1000)
    plt.scatter(W[0, 0], W[1, 0], c='b')
    plt.scatter(W[0, -1], W[1, -1], c='g')
    plt.plot(W[0, :], W[1, :], 'r-')
    plt.text(W[0, 0] + 0.1, W[1, 0], '(%.2f, %.2f)' % (W[0, 0], W[1, 0]))
    plt.text(W[0, -1] + 0.1, W[1, -1], '(%.2f, %.2f)' % (W[0, -1], W[1, -1]))
    plt.show()