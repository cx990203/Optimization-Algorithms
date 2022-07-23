# -------------------------------------------------
# 牛顿法求解the Beale Function最小值
# -------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


# Beale函数
def function(x):
    return (1.5 - x[0] + x[0] * x[1]) ** 2 + (2.25 - x[0] + x[0] * x[1] ** 2) ** 2 + (2.625 - x[0] + x[0] * x[1] ** 3) ** 2


# 梯度方向
def grad(x):
    return np.array([2 * (1.5 - x[0] + x[0] * x[1]) * (-1 + x[1]) +
                    2 * (2.25 - x[0] + x[0] * x[1] ** 2) * (-1 + x[1] ** 2) +
                    2 * (2.625 - x[0] + x[0] * x[1] ** 3) * (-1 + x[1] ** 3),
                    2 * (1.5 - x[0] + x[0] * x[1]) * x[0] +
                    2 * (2.25 - x[0] + x[0] * x[1] ** 2) * 2 * x[0] * x[1] +
                    2 * (2.625 - x[0] + x[0] * x[1] ** 3) * 3 * x[0] * x[1] ** 2], dtype=np.float)


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
    flag = 0        # 满足条件标志位，如果满足条件在，则为真
    # 采用二分法求解步长，a为前边界，b为后边界
    a = 0
    b = alpham
    alpha = 0       # 计算得到步长
    gk = df(x)      # xk位置梯度
    phi0 = f(x)
    dphi0 = np.dot(gk, p)
    while flag == 0:
        phi = f(x + alpha * p)      # 计算f(xk+1)
        gk1 = df(x + alpha * p)     # 更新梯度信息
        dphi = np.dot(gk1, p)       # 计算梯度在下降方向上的映射
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


def getAlpha(f, p, x, alpham):
    alpha = 0
    fxmin = f(x)
    for i in range(0, 100):
        if fxmin > f(x + alpham * (i / 100.0) * p):
            alpha = alpham * (i / 100.0)
            fxmin = f(x + alpha * p)
    return alpha


# Hessian矩阵
def hess(x):
    h1 = np.array([
        [-2 + 2 * x[1], 3 - 4 * x[0] + 4 * x[0] * x[1]],
        [3 - 4 * x[0] + 4 * x[0] * x[1], 2 * x[0] ** 2]
    ], dtype=np.float)
    h2 = np.array([
        [(-2 + 2 * x[1] ** 2) * (-1 + x[1] ** 2), 9 * x[1] - 8 * x[0] * x[1] + 8 * x[0] * x[1] ** 3],
        [9 * x[1] - 8 * x[0] * x[1] + 8 * x[0] * x[1] ** 3, 9 * x[0] - 4 * x[0] ** 2 + 12 * x[0] ** 2 * x[1] ** 2]
    ], dtype=np.float)
    h3 = np.array([
        [(-2 + 2 * x[1] ** 3) * (-1 + x[1] ** 3), 15.75 * x[1] ** 2 - 12 * x[0] * x[1] ** 2 + 12 * x[0] * x[1] ** 5],
        [15.75 * x[1] ** 2 - 12 * x[0] * x[1] ** 2 + 12 * x[0] * x[1] ** 5, 31.5 * x[0] * x[1] - 12 * x[0] ** 2 * x[1] + 30 * x[0] ** 2 * x[1] ** 4]
    ], dtype=np.float)
    return h1 + h2 + h3


# 牛顿法迭代过程
def newton(x0):
    maxk = 10000  # 设置最大次数
    W = np.zeros((2, maxk + 1))  # 结果记录buffer
    W[:, 0] = x0
    x = x0  # 设置起始点
    i = 0  # 记录迭代次数
    df_max = 1e-5  # 停止迭代时梯度阈值
    while np.linalg.norm(grad(x)) > df_max and i < maxk:
        H = hess(x)     # 求解hession矩阵
        p = -np.dot(np.linalg.inv(H), grad(x))  # 计算前进方向
        # alpha = wolfe(function, grad, p, x, 1, 0.1, 0.9)  # wolfe条件计算步长
        # alpha = getAlpha(function, p, x, 0.01)
        # x += alpha * p  # 计算新的迭代点
        x += p  # 计算新的迭代点
        W[:, i + 1] = x     # 记录当前位置
        i += 1      # 计算迭代次数
        print(f'{i} -- grad:{np.linalg.norm(grad(x))} -- x:{x} -- f(x):{function(x)}')
    print(f"迭代次数为：{i}")
    print(f"近似解为：{x}")
    print(f"函数值为：{function(x)}")
    print(f"当前位置梯度范数：{np.linalg.norm(grad(x))}")
    W = W[:, 0: i + 1]
    return W


if __name__ == "__main__":
    x0 = np.array([-1.2, 1], dtype=np.float)
    W = newton(x0)

    X1 = np.arange(-1.5, 3.2, 0.05)
    X2 = np.arange(-0, 2, 0.05)
    [x1, x2] = np.meshgrid(X1, X2)
    f = (1.5 - x1 + x1 * x2) ** 2 + (2.25 - x1 + x1 * x2 ** 2) ** 2 + (2.625 - x1 + x1 * x2 ** 3) ** 2
    plt.contour(x1, x2, f, 1000)
    plt.scatter(W[0, 0], W[1, 0], c='b')
    plt.scatter(W[0, -1], W[1, -1], c='g')
    plt.plot(W[0, :], W[1, :], 'r-')
    plt.text(W[0, 0] + 0.1, W[1, 0], '(%.2f, %.2f)' % (W[0, 0], W[1, 0]))
    plt.text(W[0, -1] + 0.1, W[1, -1], '(%.2f, %.2f)' % (W[0, -1], W[1, -1]))
    plt.show()

